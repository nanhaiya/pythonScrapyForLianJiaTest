# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class LianjiaSpiderPipeline(object):
    index = 0
    def __init__(self):
        self.file=open("二手房数据.csv","a",encoding="gbk")
        if self.index==0:          #第一次打开，写入头信息
            column_name="描述,价格(万元),户型,面积,朝向,电梯,产权信息\n"
            self.file.write(column_name)
            self.index = 1

    def process_item(self, item, spider):
        home_Info=item["name"]+","+ \
                  item["money"] + "," +\
                item["type"]+","+ \
                item["size"] + "," + \
                item["caoXiang"] + "," + \
                  item["DianTi"] + "," +\
                item["chanQuan"] +"\n"
        print(home_Info)
        self.file.write(home_Info)
        return item

    def closr_spider(self, spider):
        self.fp.close()
        self.file.close()