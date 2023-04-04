import pandas as pd
import requests
from bs4 import BeautifulSoup


databaseCascavel = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Cascavel/airbnb-Cascavel-filtrado.xlsx")

databaseCuritiba = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Curitiba/airbnb-Curitiba-filtrado.xlsx")

databaseLondrina = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Londrina/airbnb-Londrina-filtrado.xlsx")

databaseFoz = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Foz/airbnb-foz-do-iguacu.xlsx")

databaseMatinhos = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Matinhos/airbnb-praia-de-matinhos.xlsx")

databaseGuaratuba = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Guaratuba/airbnb-Guaratuba-filtrado.xlsx")

databaseParana1 = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Parana/airbnb-Parana1-filtrado.xlsx")
databaseParana2 = pd.read_excel("/home/guii0406/Documentos/Aprendizado_de-maquina/Databases/Parana/airbnb-Parana2-filtrado.xlsx")

databaseCascavel['Lugar'] = databaseCascavel['Lugar'].str.replace("Centro", "Cascavel")
databaseCuritiba['Lugar'] = databaseCuritiba['Lugar'].str.replace("Centro", "Curitiba")
databaseLondrina['Lugar'] = databaseLondrina['Lugar'].str.replace("Centro", "Londrina")
databaseFoz['Lugar'] = databaseFoz['Lugar'].str.replace("Centro", "Foz do iguaçu")
databaseMatinhos['Lugar'] = databaseMatinhos['Lugar'].str.replace("Centro", "Matinhos")

databaseParana1 = databaseParana1[databaseParana1['Lugar'] != 'Centro']
databaseParana2 = databaseParana2[databaseParana2['Lugar'] != 'Centro']


fullDatabase = pd.concat([databaseCascavel, databaseCuritiba, databaseLondrina, databaseFoz, databaseMatinhos, databaseGuaratuba, databaseParana1, databaseParana2])

#removendo colunas
fullDatabase = fullDatabase.drop("Unnamed: 0.1", axis=1)
fullDatabase = fullDatabase.drop("Unnamed: 0", axis=1)


#avaliação
fullDatabase['Avaliação'] = fullDatabase['Avaliação'].str.replace(",", ".")
fullDatabase["Avaliação"] = fullDatabase['Avaliação'].astype(float)

#preço
fullDatabase['Preço'] = fullDatabase['Preço'].str.replace("R", "")
fullDatabase['Preço'] = fullDatabase['Preço'].str.replace("$", "")
fullDatabase['Preço'] = fullDatabase['Preço'].str.replace(".", "")
fullDatabase["Preço"] = fullDatabase['Preço'].astype(int)

#quartos
fullDatabase['Quartos'] = fullDatabase['Quartos'].str.replace(" quarto", "")
fullDatabase['Quartos'] = fullDatabase['Quartos'].str.replace("Estúdio", "1")
fullDatabase['Quartos'] = fullDatabase['Quartos'].str.replace("s", "")
fullDatabase["Quartos"] = fullDatabase['Quartos'].astype(int)

#banheiros
fullDatabase['Banheiros'] = fullDatabase['Banheiros'].str.replace(" e meio", "")
fullDatabase['Banheiros'] = fullDatabase['Banheiros'].str.replace(" compartilhado", "")
fullDatabase['Banheiros'] = fullDatabase['Banheiros'].str.replace(" privado", "")
fullDatabase['Banheiros'] = fullDatabase['Banheiros'].str.replace("banheiro", "")
fullDatabase['Banheiros'] = fullDatabase['Banheiros'].str.replace("s", "")
fullDatabase["Banheiros"] = fullDatabase['Banheiros'].astype(int)

#hóspedes
fullDatabase['Hospedes'] = fullDatabase['Hospedes'].str.replace(" hóspedes", "")
fullDatabase['Hospedes'] = fullDatabase['Hospedes'].str.replace(" hóspede", "")
fullDatabase['Hospedes'] = fullDatabase['Hospedes'].str.replace("Mais de ", "")
fullDatabase["Hospedes"] = fullDatabase['Hospedes'].astype(int)

#camas
fullDatabase['Camas'] = fullDatabase['Camas'].str.replace(" camas", "")
fullDatabase['Camas'] = fullDatabase['Camas'].str.replace(" cama", "")
fullDatabase["Camas"] = fullDatabase['Camas'].astype(int)


newPrices = []
for e in fullDatabase['Link'].values:
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


fullDatabase['Preço certo'] = newPrices


fullDatabase.to_excel("DATABASE.xlsx")



