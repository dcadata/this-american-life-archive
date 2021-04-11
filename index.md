# Link Archive and Unofficial RSS Feed for *This American Life* Podcast Episodes 1 through Current

## ***ANNOUNCEMENT***

### As of 08 Sep 2020, THIS FEED IS NO LONGER MAINTAINED. PLEASE USE THE FEED AT (https://static.awk.space/tal.xml)[https://static.awk.space/tal.xml] (no affiliation). Thank you!

***

* ## [Unofficial RSS Feed](http://dcadata.github.io/this-american-life-archive/TALArchive.xml)
  * ### This is a valid RSS feed that you can subscribe to with your podcatcher of choice!
  * Unofficial RSS feed for the "This American Life" podcast, going back to the very first episode! Updated Mondays in MP3 format. Visit [ThisAmericanLife.org](http://www.thisamericanlife.org) for more information about the podcast.
  * [View XML on GitHub](https://github.com/dcadata/this-american-life-archive/blob/master/TALArchive.xml)

* **CSV - [view on GitHub](https://github.com/dcadata/this-american-life-archive/blob/master/TALArchive.csv) or [download](TALArchive.csv)**

* [Index/table of all episodes](https://github.com/dcadata/this-american-life-archive/blob/master/TALArchive.md)

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

[A list of missing episodes is here.](https://github.com/dcadata/this-american-life-archive/blob/master/ref_missing_eps_list.txt)

Each week, the script attempts to automatically clear the missing episodes by finding audio file URLs for them.

11/11/2019- An error was previously made in identifying missing episodes. Missing episodes can now be identified (if they arise) and will attempt to be cleared each week.

### Why are there multiple entries for some episodes?

~~If an episode's audio file is accessible at multiple URLs, each URL is listed as a separate entry for the same episode. That way, you have your choice of URLs if one goes down.~~

As of 7/31/2019, each episode now only has one URL. If that URL goes down, it will automatically find another one on the next run (the following Sunday evening).

### What if an episode becomes inaccessible in the future?

This is a possibility. For now, I have a script that checks back through old file URLs each week to make sure they are still accessible. If not, it will check the other 13 possible URLs until it finds a copy of the file.

***

**Tools Used:** Python - requests, Beautiful Soup, Pandas

***

**Contact:** [devon@ankar.io](mailto:devon@ankar.io)

***

**Last Updated:** Nov. 11, 2019
