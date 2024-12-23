import scrapy
from scrapy.loader import ItemLoader
from varredor_de_sites.items import CitacaoItem

class GoodReadsSpider(scrapy.Spider):
    # Identidade
    name = 'quotebot'
    # Request
    def start_requests(self):
        urls = ['https://www.goodreads.com/quotes']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        # Aqui é onde você deve processar o que é retornado da response
        for elemento in response.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=CitacaoItem(),
                                selector=elemento, response=response)
            loader.add_xpath('frase', ".//div[@class='quoteText']/text()")
            loader.add_xpath('autor', ".//span[@class='authorOrTitle']/text()")
            loader.add_xpath('tags', ".//div[@class='greyText smallText left']/a/text()")
            yield loader.load_item()

        # Encontrar o link para a próxima página
        next_page = response.xpath("//a[@class='next_page']/@href").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)