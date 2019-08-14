---
layout: nosidebar
redirect_from: "/tal/"
---

# *This American Life* Podcast Archive - Links/RSS Feed

# Official Download Links for Episodes 1 through Current

* ### [Unofficial RSS Feed](http://dcadata.github.io/this-american-life-archive/TALArchive.xml)
  * **This is a valid RSS feed that you can subscribe to with your podcatcher of choice!**
  * Unofficial RSS feed for the "This American Life" podcast, going back to the very first episode! Updated Mondays in MP3 format. Visit [ThisAmericanLife.org](http://www.thisamericanlife.org) for more information about the podcast.
  * **[View XML on GitHub](https://github.com/dcadata/dcadata.github.io/blob/master/this-american-life-archive/TALArchive.xml)**

* ### [Index/table of all episodes](https://github.com/dcadata/dcadata.github.io/blob/master/this-american-life-archive/TALArchive.md)

* ### CSV - [view on GitHub](https://github.com/dcadata/dcadata.github.io/blob/master/this-american-life-archive/TALArchive.csv) or [download](TALArchive.csv)

***

## What is this?

*[This American Life](http://www.thisamericanlife.org/)* is a radio show/podcast published by WBEZ Chicago Public Radio. The podcast's [official RSS feed](http://feed.thisamericanlife.org/talpodcast) only serves the most recent 5-10 episodes. However, all podcast episodes are freely and publicly available on the podcast's official website. Older episodes fall off the official RSS feed, but they are still freely available.

This project simply scrapes the URLs for those older podcast episodes that are still available but have fallen off the official RSS feed. (I am not, and will not be, hosting any *This American Life* audio files. This is only an archive of *links*, not *files*!)

***

## Process

This project was completed by automatically scraping up to 14 URLs for each of almost 700 episodes until an audio file was found for each episode in the archive. I essentially automated a process many listeners already do manually when they want to listen to an older episode. A given episode's audio file may sit at one of 14 different URLs, and the URL choice varies from episode to episode.

I also used the official short URL (`tal.fm/{episode number}`) to scrape information about each episode, currently including the episode title, description, and published date/airdate. File URLs and info for new episodes will be collected from the official RSS feed as new episodes are released.

***

## FAQ

### Why are some episodes missing?

~~Audio files couldn't be located for 7 episodes, so those 7 episodes are missing audio files. If they are ever republished in the RSS feed, they will be added at that time.~~

As of 7/31/2019, there are no missing episodes.

### Why are there multiple entries for some episodes?

~~If an episode's audio file is accessible at multiple URLs, each URL is listed as a separate entry for the same episode. That way, you have your choice of URLs if one goes down.~~

As of 7/31/2019, each episode now only has one URL. If that URL goes down, it will automatically find another one on the next run (the following Sunday evening).

### What if an episode becomes inaccessible in the future?

This is a possibility. For now, I have a script that checks back through old file URLs each week to make sure they are still accessible. If not, it will check the other 13 possible URLs until it finds a copy of the file.

### Can you post the code?

Yes, I plan to post it in the near future.

***

**Tools Used:** Python - requests, Beautiful Soup, Pandas

***

**Contact:** [devon@ankar.io](mailto:devon@ankar.io)

***

**Last Updated:** July 31, 2019 (Project)
