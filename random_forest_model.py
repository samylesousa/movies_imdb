import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import os
import numpy as np


#lendo o arquivo do dataframe
filmes = pd.read_csv('arquivos/dataframe_modificado.csv', index_col=0)
filmes = filmes.dropna()

pd.options.mode.chained_assignment = None

y = filmes["IMDB_Rating"]
X = filmes[["Meta_score", "No_of_Votes", "Gross", "Runtime"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

modelo = RandomForestRegressor(n_estimators=900, max_features=3, max_samples=60, oob_score=True)
modelo_treinado = modelo.fit(X_train, y_train)

#plotando a correlação das variáveis para analisar quais devem ser escolhidas durante o refinamento
fig, ax = plt.subplots()
ax.barh(modelo_treinado.feature_names_in_, modelo_treinado.feature_importances_, label=modelo_treinado.feature_importances_)
ax.set_ylabel("Variáveis")
ax.set_xlabel("Valor de correlação")
ax.set_title('Valores de correlação entre as variáveis')
path_grafico1 = os.path.join("graficos_gerados/random_forest", "valores_correlacao.png")
plt.savefig(path_grafico1, dpi=500) 
plt.close()

#previsão das notas
pred_nota = modelo_treinado.predict(X_test)

#calculando os valores de MAE (erro médio absolute) e RMSE (erro quadrático médio)
media = mean_absolute_error(y_true=y_test, y_pred=pred_nota)
mae = mean_squared_error(y_true=y_test, y_pred=pred_nota)
rmse = math.sqrt(mae)

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")


#plotando um gráfico para comparar os valores reais e os valores do modelo
plt.scatter(y_test, pred_nota)
plt.xlabel("Valores Reais")
plt.ylabel("Valores do Modelo")
plt.title("Real vs Modelo")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], "r--")

path_grafico2 = os.path.join("graficos_gerados/random_forest", "resultados_modelo.png")
plt.savefig(path_grafico2, dpi=500) 
plt.close()

#aplicando validação cruzada para avaliar o desempenho de um modelo
print(f"R² médio: {cross_val_score(modelo, X_train, y_train, cv=10, n_jobs=-1).mean()}")
print(f"MAE médio: {-cross_val_score(modelo, X_train, y_train, cv=10, n_jobs=-1, scoring='neg_mean_absolute_error').mean()}")
print(f"RMSE médio: {np.sqrt(-cross_val_score(modelo, X_train, y_train, cv=10, scoring='neg_mean_squared_error', n_jobs=-1)).mean()}")

#salvando o modelo já treinado em um arquivo
with open("modelagem/random_forest.pkl", "wb") as f:
	pickle.dump(modelo_treinado, f)