# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
import datetime
import json
# from sex.config import Dbconfig
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy import log
import re
import urllib
import urllib2
import os
import threading

class SexPipeline(object):

    def __init__(self):
        #self.conn = MySQLdb.connect(user = Dbconfig['user'], passwd = Dbconfig['passwd'], db = Dbconfig['db'],
        #                            host = Dbconfig['host'], charset = 'utf8', use_unicode = True)
        #self.cursor = self.conn.cursor()

        self.file = open('sex.json', 'wb')



    def process_item(self, item, spider):
        curTime = datetime.datetime.now()
        # try:
            # self.cursor.execute(
            #     """INSERT IGNORE INTO SEX_ARTICLE(title, pic_count, url, author, up_date, update_time,record_time)
            #     VALUES(%s, %s, %s, %s, %s, %s)
            #     """,
            #     (
            #         item['title'],
            #         item['pic_count'],
            #         item['url'],
            #         item['author'],
            #         item['up_date'],
            #         item['record_time'],
            #         curTime
            #     )
            # )
            #
            # self.conn.commit()

        # except MySQLdb.Error , e:
        #     print('Error %d %s' %(e.args[0], e.args[1]))
        line = "%s \t%s\n"%(item['title'], item['url'])
        # self.file.write(line)
        download = downloadTread(item)
        download.start();

        return item





class downloadTread(threading.Thread):
    def __init__(self, item):
        threading.Thread.__init__(self)
        self.item = item

    def run(self):
        path = '/Users/xxx/Desktop/aaa/';
        folder = path + self.item['title'].strip()

        if not os.path.exists(folder):
            os.mkdir(folder)

        for img in self.item['image_urls']:
            filename = re.findall(r'/\d+\.[a-z]*', img.encode('utf-8'))

            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
            req = urllib2.Request(img.encode('utf-8'), headers=hdr)

            try:
                img = urllib2.urlopen(req)
                f = open(folder + filename[0], "wb")
                f.write(img.read())
                f.close()
            except urllib2.HTTPError, e:
                print e.fp.read()