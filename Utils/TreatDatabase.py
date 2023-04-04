import pandas as pd
import requests
from bs4 import BeautifulSoup

data = pd.read_excel(r'C:\Users\Gui\Documents\Aprendizado_de-maquina\DATABASE.xlsx')
data = data.drop("Unnamed: 0", axis=1)

newPrices = []
for e in data['Link'].values:
    try:
        url = requests.get(f"https://www.airbnb.com.br/{e}")
        soup = BeautifulSoup(url.content, 'html.parser')
        info = str(soup.find('meta', attrs={'name': 'description'}))
        price = info.split('$')[1].split('.')[0]
        newPrices.append(price)
        print(price)
    except Exception as e:
        newPrices.append("excluido")
        print("exluido")
        
data['Preço certo'] = newPrices


data['Preço'] = data['Preço certo']

data = data.drop("Preço certo", axis=1)

data = data.drop_duplicates(subset=['Tipo', 'Lugar', 'Avaliação','Quantidade de avaliações', 'Preço', 'Hospedes','Quartos', 'Camas', 'Banheiros'])
data = data[data['Preço'] != 'excluido']
data = data[data['Preço'] != '9999']
data["Preço"] = data['Preço'].astype(int)

data.to_excel("DATABASE.xlsx")
