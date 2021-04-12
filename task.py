from datetime import datetime
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup as BS
from requests import get


class Reader:
    _data_dir = 'data/'
    _raw_fp = _data_dir + 'raw.csv'
    _transformed_fp = _data_dir + 'transformed.csv'
    _exceptions_fp = _data_dir + 'missing.csv'

    @property
    def raw(self):
        dtypes = self._dtypes.copy()
        del dtypes['pubdate_timestamp']
        return pd.read_csv(self._raw_fp, dtype=dtypes)

    @property
    def _transformed(self):
        return pd.read_csv(self._transformed_fp, dtype=self._dtypes)

    @property
    def _exceptions(self):
        return pd.read_csv(self._exceptions_fp, dtype={'num': int, 'exc': str})

    @property
    def _dtypes(self):
        return {
            'num': int,
            'url': str,
            'full_url': str,
            'title': str,
            'description': str,
            'pubdate': str,
            'pubdate_timestamp': int,
            'download_url': str,
        }

    @property
    def _str_fields(self):
        return ['url', 'full_url', 'title', 'description', 'pubdate', 'download_url']


class Requester(Reader):
    def __init__(self, **kwargs):
        self._nums = kwargs.get('nums')
        self._new = []
        self._exc = []

    def make_requests(self):
        for num in self._nums:
            try:
                self._new.append(_make_one_request(num))
            except Exception as exc:
                self._exc.append({
                    'num': num,
                    'exc': str(exc),
                })
            sleep(1)

    def save_raw(self, overwrite=None):
        new = pd.DataFrame(self._new)
        df = new if overwrite else pd.concat((new, self.raw))
        df.to_csv(self._raw_fp, index=False)
        pd.DataFrame(self._exc).to_csv(self._exceptions_fp, index=False)


class Episode:
    def __init__(self, **kwargs):
        self._text = kwargs.get('text')

    @property
    def data(self):
        title_section = self._soup.find('div', class_='episode-title')
        container = title_section.find_parent('div', class_='container')

        try:
            description = container.find('div', class_='field-name-body').text
        except AttributeError:
            description = ''

        data = {
            'pubdate': container.find('div', class_='meta').find('div', class_='field-name-field-radio-air-date').find(
                'span', class_='date-display-single').text,
            'title': title_section.find('h1').text,
            'description': description,
            'download_url': container.find('ul', class_='actions').find('li', class_='download').find('a').get('href'),
        }
        return data

    @property
    def _soup(self):
        return BS(self._text, 'lxml')


class Writer(Requester):
    def transform_and_write(self):
        df = self._transform()
        df.to_csv(self._transformed_fp, index=False)
        open('TALArchive.xml', 'w').write(self._write_xml(df))

    def _transform(self):
        df = self.raw.copy()
        for col in self._str_fields:
            df[col] = df[col].fillna(' ').apply(lambda x: x.strip()).apply(lambda x: x.replace('\u02bc', '')).replace(
                '&', '\&')
        df.download_url = df.download_url.apply(lambda x: x.split('?', 1)[0])
        df['pubdate_timestamp'] = df.pubdate.apply(pd.to_datetime).apply(lambda x: x.timestamp()).apply(int)
        df = df.sort_values('pubdate_timestamp', ascending=False).drop_duplicates(subset=['num'])
        return df[list(self._dtypes)]

    @staticmethod
    def _write_xml(df):
        _read = lambda x: open(f'templates/{x}.xml').read()
        item_xml = _read('item')
        items_xml = '\n'.join((item_xml.format(**record) for record in df.to_dict('records')))
        xml_output = _read('feed').format(
            items=items_xml, feed_last_updated=datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        return xml_output


def _make_one_request(num):
    url = f'https://www.thisamericanlife.org/episode/{num}'
    r = get(url)
    assert r.ok
    data = {
        'num': num,
        'url': url,
        'full_url': r.url,
    }
    data.update(Episode(text=r.text).data)
    return data


def _get_latest_episode_number():
    r = get('http://feed.thisamericanlife.org/talpodcast')
    sleep(1)
    soup = BS(r.text, 'lxml')
    return int(soup.find('item').find('title').text.split(':', 1)[0])


def main():
    latest_num = _get_latest_episode_number()
    writer = Writer(nums=(latest_num,))
    if latest_num not in set(writer.raw.num):
        writer.make_requests()
        writer.save_raw()
    writer.transform_and_write()


if __name__ == '__main__':
    main()
