# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
pd.options.display.max_rows = 99999999999999
import requests

url = requests.get("https://www.airbnb.com.br/rooms/751553567428761524?adults=1&children=0&enable_m3_private_room=false&infants=0&pets=0&check_in=2023-04-09&check_out=2023-04-14&federated_search_id=a17ac39a-2355-41e3-80c4-5c26709204d9&source_impression_id=p3_1680570297_XF%2BxYzXafuJ%2BOJX6")

soup = BeautifulSoup(url.content, 'html.parser')

info = str(soup.find('meta', attrs={'name': 'description'}))

info = info.split('$')[1].split('.')[0]

print(info)


