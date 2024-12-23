# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join

def tirar_espaco_em_branco(valor):
    return valor.strip()

def botar_maiusculo(valor):
    return valor.upper()

def processar_carateres_especiais(valor):
    return valor.replace(u"\u2019", '')

def mudar_virgula_por_ponto_evirgula(valor):
    return valor.replace(',', ';')

class CitacaoItem(scrapy.Item):
    frase = scrapy.Field(
        input_processor=MapCompose(
            tirar_espaco_em_branco, processar_carateres_especiais),
        output_processor=TakeFirst()
    )
    autor = scrapy.Field(
        input_processor=MapCompose(tirar_espaco_em_branco, botar_maiusculo),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(';')
    )

     
