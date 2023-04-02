# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas as pd
pd.options.display.max_rows = 99999999999999
import requests
import json
import time
#variável para armazenar o domínio do Airbnb
airbnbDomain = "https://www.airbnb.com.br"

#request para primeira página
page = requests.get("https://www.airbnb.com.br/s/Matinhos-~-PR/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=Matinhos%20-%20PR&place_id=ChIJ8SCG7y3u25QRVTkDb8dp8OE&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click")

#criando lista de estabelecimentos
estabelecimentos = []

#loop para iterar todas as 15 páginas disponíveis
for x in range(15):
    
    #Transformando a string html para HTML de fato
    soup = BeautifulSoup(page.content, 'html.parser')
    
    #atribuindo os estabelecimentos encontrados à partir da classe HTML para uma lista
    lista = soup.find_all('div', attrs={'class': 'c4mnd7m dir dir-ltr'})

    #iterando sobre todos os estabelecimentos da páginas.
    for estabelecimento in lista:
        estabelecimento_data = []

        #Atribundo os dados de cada estabelecimento para a variavel estabelecimento_data
        estabelecimento_data.append(estabelecimento.find(name='div', attrs={'class': 't1jojoys dir dir-ltr'}).text)#nome
        estabelecimento_data.append(estabelecimento.find(name='span', attrs={'class': '_14y1gc'}).text)#preco
        #tratando exceção que ocorre quando o estabelecimento não possui avaliação nenhuma, deixando o campo vazio
        try:
            estabelecimento_data.append(estabelecimento.find(name='span', attrs={'class': 'r1dxllyb dir dir-ltr'}).text)#avaliacao
        except:
            print("sem avaliacao")
            estabelecimento_data.append(' ')
        link = estabelecimento.find('a', attrs={'class': 'l1j9v1wn bn2bl2p dir dir-ltr'}).get("href")

        #loop para ficar tentando conseguir os dados internos de cada estabelecimento
        key = False
        while key == False:
            page = requests.get(airbnbDomain + link)
            soupp = BeautifulSoup(page.content, 'html.parser')
            content = soupp.find(name='script', attrs={'id': 'data-state'}).text
            contentjson = json.loads(content)

            try:
                data = contentjson['niobeMinimalClientData'][1][1]['data']['presentation']['stayProductDetailPage']['sections']['sections'][12]['section']['detailItems']
                for item in data:
                    estabelecimento_data.append(item['title'])
                key = True
                print('foi')
            except Exception as e:
                print('não foi')
                key = False


        estabelecimento_data.append(link)#link
        #atribuindo cada estabelecimento para o array de estabelecimentos
        estabelecimentos.append(estabelecimento_data)

    #tratando exceção para quando acabar as páginas o loop parar
    try:
        #encontrando o botão para a próxima página e extraindo o link
        next = soup.find('a', attrs={'class': 'l1j9v1wn c1ytbx3a dir dir-ltr'}).get("href")
        print("deu boa")
    except:
        print("deu ruim")
        break

    #request para próxima página
    page = requests.get(airbnbDomain + next)
    time.sleep(10)

#Criando o dataframe baseado no array de estabelecimentos
tabela = pd.DataFrame(estabelecimentos, columns=['nome', 'Preço', 'avaliação',"Hospedes","Quartos","Camas","Banheiros", "Link"])

#Separando o Tipo de estabelecimento da cidade
tabela[['Tipo','Lugar']] = tabela['nome'].str.split(" em ", expand = True)
tabela = tabela.drop(columns=['nome'])

#formatando a coluna de preço
tabela['Preço'] = tabela['Preço'].str.split(' ').str[0]

#Separando a avaliação da quantidade de avaliações
tabela[['Avaliação','Quantidade de avaliações']] = tabela['avaliação'].str.split(" ", expand = True)
tabela = tabela.drop(columns=['avaliação'])

#formatando a coluna de quantidade de avaliações
tabela['Quantidade de avaliações'] = tabela['Quantidade de avaliações'].str.replace("(", "")
tabela['Quantidade de avaliações'] = tabela['Quantidade de avaliações'].str.replace(")", "")

#Reposiocinando colunas
tabela = tabela[['Tipo', "Lugar", 'Avaliação', "Quantidade de avaliações", "Preço", "Hospedes","Quartos","Camas","Banheiros","Link"]]

# exportando para xlsx
tabela.to_excel('airbnb-matinhos-1.xlsx')

