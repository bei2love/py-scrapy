# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import MySQLdb
import datetime
import json
# from sex.config import Dbconfig

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
        self.file.write(line)
        return item
