# pip install Flask
from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
# import webview

app = Flask(__name__)
# window = webview.create_window('teste', app, width=1920, height=1080)



@app.route("/",  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tipo = request.form.get('tipo_')
        lugar = request.form.get('lugar_')
        avaliacao = request.form.get('avaliacao')
        quantiAvalicao = request.form.get('quantiAvalicao')
        hospedes = request.form.get('hospedes')
        quartos = request.form.get('quartos')
        camas = request.form.get('camas')
        banheiros = request.form.get('banheiros')
        
        value = predict(tipo, lugar, avaliacao, quantiAvalicao, hospedes, quartos, camas, banheiros)
        return render_template('result.html',value=value)



    return render_template('index.html')


def predict(tipo_, lugar_, avaliacao_, quantiAvalicao_, hospedes_, quartos_, camas_, banheiros_):
    # https://towardsdatascience.com/xgboost-fine-tune-and-optimize-your-model-23d996fab663

    import pandas as pd
    import xgboost as xgb
    from sklearn.model_selection import train_test_split

    # Carrega os dados do arquivo Excel
    df = pd.read_excel('DATABASE-UPDATE-LUGARES2.xlsx')

    # Seleciona as colunas necessarias
    X = pd.get_dummies(df[['Tipo', 'Lugar', 'Avaliação', 'Quantidade de avaliações', 'Hospedes', 'Quartos', 'Camas', 'Banheiros', 'Link']])
    y = df['Preço']

    # Divide os dados em conjuntos de treinamento e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Define o modelo XGBoost com os hiperparâmetros especificados
    xg_reg = xgb.XGBRegressor(objective='reg:squarederror',n_estimators=500, max_depth=6, min_child_weight=0.8, colsample_bylevel= 0.5, learning_rate=0.1)

    # Treina o modelo com os dados de treinamento
    xg_reg.fit(X_train, y_train)

    # Faz as previsões com o modelo treinado usando os dados de teste
    preds = xg_reg.predict(X_test)
    # for itemt, itemp in zip( y_test.to_list(), preds.tolist()):
    #     print(str(itemt), str(itemp))
    # Define as características do novo lugar
    novo_lugar = pd.DataFrame({'Tipo': [f'{tipo_}'], 'Lugar': [f'{lugar_}'], 'Avaliação': [avaliacao_], 'Quantidade de avaliações': [quantiAvalicao_], 'Hospedes': [hospedes_], 'Quartos': [quartos_], 'Camas': [camas_], 'Banheiros': [banheiros_]})

    # Aplica get_dummies e reindexa as colunas do novo lugar
    novo_lugar = pd.get_dummies(novo_lugar)
    novo_lugar = novo_lugar.reindex(columns=X_train.columns, fill_value=0)

    # Faz a previsão do preço do novo lugar com o modelo treinado
    previsoes = xg_reg.predict(novo_lugar)

    # Imprime o preço previsto do novo lugar com duas casas decimais
    # print('\n O preço previsto para o imóvel é: R$ {:.2f}'.format(previsoes[0]), '\n')
    print(tipo_ + ' ' + lugar_+ ' ' + avaliacao_+ ' ' + quantiAvalicao_+ ' '+ hospedes_+ ' ' + quartos_+ ' '+camas_+ ' '+banheiros_)
    return '{:.2f}'.format(previsoes[0])


if __name__ in '__main__':
    app.run(debug=True)
    # webview.start()