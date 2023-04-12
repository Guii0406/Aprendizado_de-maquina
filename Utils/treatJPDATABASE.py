import pandas as pd

# C:\\Users\\dagos\\OneDrive\\Desktop\\Aprendizado_de-maquina\\DATABASE.xlsx"

newdatabase = pd.read_excel("C:\\Users\\dagos\\Downloads\\DATABASE.xlsx")

# Curitiba
# Curitiba_
# CURITIBA
# CURITIBA_
# Curitiba Cívico
# Cidade Industrial De Curitiba
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Curitiba ", "Curitiba")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" Curitiba", "Curitiba")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("CURITIBA", "Curitiba")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("CURITIBA ", "Curitiba")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Curitiba Cívico", "Curitiba")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("CuritibaCívico", "Curitiba")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Cidade Industrial De Curitiba", "Curitiba")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Cidade Industrial DeCuritiba", "Curitiba")


# Pinhais
# Pinhais_
# São José dos Pinhais
# _São José dos Pinhais
# São José dos Pinhais_
# Borda do campo, São José dos Pinhais_
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Pinhais ", "Pinhais")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" São José dos Pinhais", "São José dos Pinhais")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("São José dos Pinhais ", "São José dos Pinhais")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Borda do campo, São José dos Pinhais ", "São José dos Pinhais")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Borda do campo,São José dos Pinhais", "São José dos Pinhais")



# Cascavel
# Cascavel_
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Cascavel ", "Cascavel")


# Foz do Iguaçu
# _Foz do Iguaçu
# Foz do Iguaçu_
# Jardim Polo Foz do iguaçu
# Foz do Iguaçu - PR
# Loteamento Parque do Patriarco, Foz do Iguaçu
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Foz do Iguaçu ", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" Foz do Iguaçu", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Foz do iguaçu ", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" Foz do iguaçu", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Foz do iguaçu", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Jardim Polo Foz do iguaçu", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Jardim PoloFoz do Iguaçu", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Foz do Iguaçu- PR", "Foz do Iguaçu")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Loteamento Parque do Patriarco,Foz do Iguaçu", "Foz do Iguaçu") 


# Guaratuba
# _Guaratuba
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" Guaratuba", "Guaratuba")


# Matinhos
# _Matinhos
# Matinhos_
# MATINHOS
# Matinhos Balneário Flórida.
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" Matinhos", "Matinhos")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Matinhos ", "Matinhos")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("MATINHOS", "Matinhos")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" Matinhos Balneário Flórida.", "Matinhos")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("MatinhosBalneário Flórida.", "Matinhos")



# Praia de Leste
# Praia de leste
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Praia de Leste", "Praia de leste")


# Londrina
# _Londrina
# Londrina_
# Londrina Londrina
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Londrina ", "Londrina")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace(" Londrina", "Londrina")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("Londrina Londrina", "Londrina")
newdatabase['Lugar'] = newdatabase['Lugar'].str.replace("LondrinaLondrina", "Londrina")

newdatabase.to_excel("DATABASE-UPDATE-LUGARES.xlsx")


