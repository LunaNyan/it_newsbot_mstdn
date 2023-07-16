#!/usr/bin/python3

from mastodon import Mastodon
from datetime import datetime
from dateutil.parser import parse
import json
import feedparser
import time

class News:
    def __init__(self, feed_name: str, title: str, url: str, timestamp: datetime):
        self.feed_name = feed_name
        self.title = title
        self.url = url
        self.timestamp = timestamp

# Open config.json
jsonFile = open("config.json", "r")
jsonContent = jsonFile.read()
jsonFile.close()
jsonObject = json.loads(jsonContent)

# Log into Mastodon
mstdn = Mastodon(
    access_token=jsonObject['access_token'],
    api_base_url=jsonObject['api_base_url']
)

newses = list()

for i in jsonObject['feeds']:
    f = feedparser.parse(f'feed:{i["url"]}')
    for idx, ii in enumerate(f['entries']):
        if parse(ii['updated']).timestamp() > jsonObject['last_checked']:
            newses.append(
                News(
                    feed_name=i['feed_name'],
                    title=ii['title'],
                    url=ii['link'],
                    timestamp=parse(ii['updated'])
                )
            )

for i in newses:
    mstdn.status_post(
        status=f'{i.feed_name} 새 소식\n{i.title}\n{i.url}',
        visibility=jsonObject['visibility']
    )
    time.sleep(5)
    print(i)

jsonObject['last_checked'] = int(datetime.now().timestamp())

jsonFile = open('config.json', 'w')
jsonFile.write(json.dumps(jsonObject, ensure_ascii=False))
jsonFile.close()
