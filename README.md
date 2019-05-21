### Welcome to my repo

This repository holds scripts and sources to run an analysis of our prime minister's speeces which are publicly available.

The speeches were downloaded from: [here](https://www.kormany.hu/hu/a-miniszterelnok/beszedek-publikaciok-interjuk)

The speeches are recorded page by page, and subpage by subpage as a dictionary. I suppose the webserver has some scrape protection as the selenium webdrivers fails to load if there is no sleep inbetween consecutive scrapes.

This is how the dictionary looks like.

``` bash
	{'pageid':
		{'url':'', 'content':[{'url':'','title':'','talk':''}]}

```