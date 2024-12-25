import scrapy

class ProxyscraperSpider(scrapy.Spider):
    # Identidade
    name = 'proxyscraperdesafio'
    # Request
    def start_requests(self):
        urls = ['https://www.free-proxy-list.net/web-proxy.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # Response
    def parse(self, response):
        # Montar um xpath que pegue cada linha
        for linha in response.xpath('//*[@id="list"]/div/div[2]/table/tbody/tr'):
            yield {
                # Montar individualmente cada item
                'Proxy Name': linha.xpath('./td[1]/a/text()').get(),
                'Domain': linha.xpath('./td[2]/text()').get(),
                'Country': linha.xpath('./td[3]/text()').get(),
                'Speed': linha.xpath('./td[4]/text()').get(),
                'Popularity': linha.xpath('./td[5]/div/div/text()').get(),
            }