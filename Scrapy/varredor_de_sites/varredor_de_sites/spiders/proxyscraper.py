import scrapy

class ProxyscraperSpider(scrapy.Spider):
    # Identidade
    name = 'proxyscraper'
    # Request
    def start_requests(self):
        urls = ['https://www.us-proxy.org/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # Response
    def parse(self, response):
        for linha in response.xpath('//*[@id="list"]/div/div[2]/div/table/tbody/tr'):
            yield {
                'IP Address': linha.xpath('./td[1]/text()').get(),
                'Port': linha.xpath('./td[2]/text()').get(),
                'Code': linha.xpath('./td[3]/text()').get(),
                'Country': linha.xpath('./td[4]/text()').get(),
                'Anonymity': linha.xpath('./td[5]/text()').get(),
                'Google': linha.xpath('./td[6]/text()').get(),
                'Https': linha.xpath('./td[7]/text()').get(),
                'Last Checked': linha.xpath('./td[8]/text()').get(),
            }