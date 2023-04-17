import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Ler o arquivo 'DATABASE.xlsx' em um DataFrame
df = pd.read_excel('DATABASE-UPDATE-LUGARES.xlsx')

# Selecionar as colunas necessarias  e criar variáveis dummy para as colunas categóricas
X = pd.get_dummies(df[['Tipo', 'Lugar', 'Avaliação', 'Quantidade de avaliações', 'Hospedes', 'Quartos', 'Camas', 'Banheiros']])

# Selecionar a coluna 'Preço' como variável dependente
y = df['Preço']

# Dividir os dados em conjuntos de treinamento e teste com uma proporção de 80% para treinamento e 20% para teste, e definir o estado aleatório como 42 para reproduzibilidade
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar um objeto LinearRegression
modelo = LinearRegression()

# Treinar o modelo com os dados de treinamento
modelo.fit(X_train, y_train)

# Fazer previsões com o modelo treinado usando os dados de teste
y_pred = modelo.predict(X_test)

# Avaliar o desempenho do modelo usando o coeficiente de determinação R²
r2_score(y_test, y_pred)

# Solicitar que o usuário insira as informações do novo imóvel
print("Insira as informações do novo imóvel:")
tipo = input("Tipo: ")
lugar = input("Lugar: ")
avaliacao = float(input("Avaliação (de 0 a 5): "))
quantidade_avaliacoes = int(input("Quantidade de avaliações: "))
hospedes = int(input("Número de hospedes: "))
quartos = int(input("Número de quartos: "))
camas = int(input("Número de camas: "))
banheiros = int(input("Número de banheiros: "))

# Criar um DataFrame com as informações do novo imóvel
novo_lugar = pd.DataFrame({
    "Tipo": [tipo],
    "Lugar": [lugar],
    "Avaliação": [avaliacao],
    "Quantidade de avaliações": [quantidade_avaliacoes],
    "Hospedes": [hospedes],
    "Quartos": [quartos],
    "Camas": [camas],
    "Banheiros": [banheiros]
})


# Criar variáveis dummy para as colunas categóricas do novo imóvel
novo_lugar = pd.get_dummies(novo_lugar)

# Reordenar as colunas do DataFrame do novo imóvel para que fiquem na mesma ordem das colunas do DataFrame de treinamento, preenchendo com 0 para as colunas ausentes
novo_lugar = novo_lugar.reindex(columns=modelo.feature_names_in_, fill_value=0)

# Fazer previsões de preço para o novo imóvel usando o modelo treinado
previsoes = modelo.predict(novo_lugar)

# Imprimir o preço previsto para o novo imóvel formatado em reais com duas casas decimais
print('O preço previsto para o imóvel é: R$ {:.2f}'.format(previsoes[0]))