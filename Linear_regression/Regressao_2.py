import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

# Carrega os dados do arquivo Excel
df = pd.read_excel('DATABASE-UPDATE-LUGARES.xlsx')

# Seleciona as colunas necessarias
X = pd.get_dummies(df[['Tipo', 'Lugar', 'Avaliação', 'Quantidade de avaliações', 'Hospedes', 'Quartos', 'Camas', 'Banheiros', 'Link']])
y = df['Preço']

# Divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define o modelo XGBoost com os hiperparâmetros especificados
xg_reg = xgb.XGBRegressor(objective='reg:squarederror', colsample_bytree=0.7, learning_rate=0.3, max_depth=8, alpha=10, n_estimators=400)

# Treina o modelo com os dados de treinamento
xg_reg.fit(X_train, y_train)

# Faz as previsões com o modelo treinado usando os dados de teste
preds = xg_reg.predict(X_test)

# Define as características do novo lugar
novo_lugar = pd.DataFrame({'Tipo': ['Casa de campo'], 'Lugar': ['Campina Grande do Sul'], 'Avaliação': [4.91], 'Quantidade de avaliações': [32], 'Hospedes': [16], 'Quartos': [4], 'Camas': [12], 'Banheiros': [3]})

# Aplica get_dummies e reindexa as colunas do novo lugar
novo_lugar = pd.get_dummies(novo_lugar)
novo_lugar = novo_lugar.reindex(columns=X_train.columns, fill_value=0)

# Faz a previsão do preço do novo lugar com o modelo treinado
previsoes = xg_reg.predict(novo_lugar)

# Imprime o preço previsto do novo lugar com duas casas decimais
print('\n O preço previsto para o imóvel é: R$ {:.2f}'.format(previsoes[0]), '\n')







