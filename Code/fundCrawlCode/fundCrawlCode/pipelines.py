# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import string

class JsonWithEncodingFundPipeline(object):
      def __init__(self):
          self.out=csv.writer(file('94.csv', 'wb')) 
          entries=['爬取序号','大学','二级学科代码','页数','学科代码','项目名称','资助金额','起止时间','负责人','详细链接']
          self.out.writerow(entries)

      def process_item(self, item, spider):
            line=[]
            keys = ['id', 'school', 'subcode','page', 'subcategory', 'itemname', 'fundmoney', 'time', 'principal', 'url']
            for key in keys:           
                value = item.get(key)  
                value=''.join(value)
                value=value.encode('utf-8')
                line.append(value)
            self.out.writerow(line)
            return item

      def spider_closed(self, spider):
            self.out.close()
