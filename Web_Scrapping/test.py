
from bs4 import BeautifulSoup
import requests
import json
import time

key = False
while key == False:
    page = requests.get('https://www.airbnb.com.br/rooms/48736735?adults=1&category_tag=Tag%3A4104&children=0&infants=0&pets=0&search_mode=flex_destinations_search&check_in=2023-05-14&check_out=2023-05-19&federated_search_id=54325eda-3382-49c6-88c2-83283ef1b85a&source_impression_id=p3_1679536972_8jU20b07qxTaa4SI')
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find(name='script', attrs={'id': 'data-state'}).text
    contentjson = json.loads(content)

    try:
        data = contentjson['niobeMinimalClientData'][1][1]['data']['presentation']['stayProductDetailPage']['sections']['sections'][12]['section']['detailItems']
        for item in data:
            print(item['title'])
        key = True
    except Exception as e:
        print(e)
        key = False


