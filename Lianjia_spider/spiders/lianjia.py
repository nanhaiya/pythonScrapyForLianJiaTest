# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Lianjia_spider import items


class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['cs.lianjia.com']
    start_urls = ['https://cs.lianjia.com/ershoufang/pg1/']

    rules = (
        Rule(LinkExtractor(allow=r'.+ershoufang/pg\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+ershoufang/\d+\.html'),callback="parse_item",follow=False)
    )

    def parse_item(self, response):
        money=response.xpath("//span[@class='total']/text()").get() #价格
        name =response.xpath("//h1[@class='main']/@title").get()  # 名称
        info=response.xpath("//div[@class='introContent']")
        baseInfo=info.xpath(".//div[@class='base']/div/ul/li/text()").getall() #基本属性

        type = baseInfo[0] # 户型
        size = baseInfo[2] # 面积
        caoXiang = baseInfo[6]  # 朝向
        DianTi = baseInfo[10] # 电梯
        jiaoYiInFo=info.xpath(".//div[@class='transaction']/div/ul/li/span/text()").getall() #交易信息
        chanQuan=""
        for j in jiaoYiInFo:
            chanQuan+=j.strip()+";"
        item=items.LianjiaSpiderItem(money=money,name=name,type=type,
                                     size=size,caoXiang=caoXiang,DianTi=DianTi,chanQuan=chanQuan)
        yield item
