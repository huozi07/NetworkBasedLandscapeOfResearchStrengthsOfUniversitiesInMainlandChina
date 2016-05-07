# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field

class FundsortItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class FundItem(Item):
    id=Field()
    itemname = Field()
    school = Field()
    subcode=Field()
    fundmoney=Field()
    subcategory=Field()
    time=Field()
    principal=Field()
    url=Field()
    page=Field()