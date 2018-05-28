# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from items import InformationItems, TweetsItem
import MySQLdb

class MysqlDBPipleline(object):
    def __init__(self):
        self.count = 1
        self.conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='llwei1',
                db='sinaweibo',
                charset='utf8',
                )
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        if isinstance(item, TweetsItem):
            try:
                print("***********at beginning of saving**********")
                sql = ''
                sql+=str('INSERT INTO sinaweibo.tweets (`_id`,`Content`,`Coordinates`)')
                sql+=str(' Values(\'' )
                sql+=str(item['_id'])
                sql+=str('\', \'')
                sql+=str(item['Content'])
                sql+=str('\', \'')
                sql+=str(item['Co_oridinates'])
                sql+=str('\', \'')
                print(sql)
                print("*********** SQL SYNTAX *********** ")
                print(''.join(sql))
                self.cur.execute(sql)
                self.conn.commit()
                print("saved")
                self.count = self.count +1
                print(self.count)
            except Exception:
                pass
        elif isinstance(item, InformationItems):
            try:
                print("***********at beginning of saving**********")
                sql = ''
                sql+=str('INSERT INTO sinaweibo.informations(`_id`,`NickName`,`Gender`,`Province`,`City`,`BriefIntroduction`) ')
                sql+=str(' Values(\'' )
                sql+=str(item['_id'])
                sql+=str('\', \'')
                sql+=str(item['NickName'])
                sql+=str('\', \'')
                sql+=str(item['Gender'])
                sql+=str('\', \'')
                sql+=str(item['Province'])
                sql+=str('\', \'')
                sql+=str(item['City'])
                sql+=str('\', \'')
                sql+=str(item['BriefIntroduction'])
                sql+=str('\', \'')
                print(sql)
                sql+=str(item['URL'])
                sql+=str('\')')
                print("*********** SQL SYNTAX *********** ")
                print(''.join(sql))
                self.cur.execute(sql)
                self.conn.commit()
                print("saved")
                self.count = self.count +1
                print(self.count)
            except Exception:
                pass
