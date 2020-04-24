# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaSpiderItem(scrapy.Item):
    money=scrapy.Field()  #价格
    name=scrapy.Field()   #名称
    type=scrapy.Field()   #户型
    size=scrapy.Field()   #面积
    caoXiang=scrapy.Field()   #朝向
    DianTi=scrapy.Field() #电梯
    chanQuan=scrapy.Field()   #产权信息
