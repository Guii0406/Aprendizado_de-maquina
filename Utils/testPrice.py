# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
pd.options.display.max_rows = 99999999999999
import requests

url = requests.get("https://www.airbnb.com.br/rooms/37631156?adults=1&children=0&enable_m3_private_room=false&infants=0&pets=0&check_in=2023-04-04&check_out=2023-04-09&federated_search_id=15de34ab-e06a-4a87-936d-d36ed0f66044&source_impression_id=p3_1680576408_IdLj7g0H8UkOzS9K")

soup = BeautifulSoup(url.content, 'html.parser')

info = str(soup.find('meta', attrs={'name': 'description'}))

# info = info.split('$')[1].split('.')[0]

print(info)


