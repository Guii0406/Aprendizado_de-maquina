import pandas as pd


df = pd.read_excel("DATABASE.xlsx")


tipos = df['Tipo'].unique().tolist()

lugares = df['Lugar'].unique().tolist()

print(lugares)


with open('lugarex.txt', 'w') as lugarestxt:
    for l in lugares:
        lugarestxt.write(f'<option value="{l}">{l}</option>\n')

with open('tipos.txt', 'w') as tipostxt:
    for t in tipos:
        tipostxt.write(f'<option value="{t}">{t}</option>\n')


