import pandas as pd
import numpy as np

#matinhos caminho - C:\Users\dagos\OneDrive\Desktop\Aprendizado_de-maquina\airbnb-matinhos-1.xlsx

#foz = pd.read_excel("C:\\Users\\dagos\\OneDrive\\Desktop\\Aprendizado_de-maquina\\airbnb-foz.xlsx")

# carrega a tabela
tabela = pd.read_excel("C:\\Users\\dagos\\OneDrive\\Desktop\\Aprendizado_de-maquina\\airbnb-matinhos-1.xlsx")

# remove as linhas que contêm pelo menos uma célula vazia
tabela_sem_vazios = tabela.dropna()

# remove as linhas que contêm o valor "(Total sem impostos)" na coluna "preço"
tabela_sem_vazios_e_total_sem_impostos = tabela_sem_vazios[tabela_sem_vazios['Preço'] != 'Total sem impostos:']

# imprime a nova tabela sem as linhas com células vazias e sem o valor "(Total sem impostos)" na coluna "preço"
print(tabela_sem_vazios_e_total_sem_impostos)

tabela_sem_vazios_e_total_sem_impostos.to_excel('airbnb-praia-de-matinhos.xlsx')
