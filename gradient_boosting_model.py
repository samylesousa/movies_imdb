import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor
import os


#lendo o arquivo do dataframe
filmes = pd.read_csv('arquivos/dataframe_modificado.csv', index_col=0)
filmes = filmes.dropna()

pd.options.mode.chained_assignment = None

#convertendo os valores categóricos em numericos para facilitar a modelagem
le = LabelEncoder()
filmes.Certificate = le.fit_transform(filmes.Certificate)
filmes.Director = le.fit_transform(filmes.Director)
filmes.Star1 = le.fit_transform(filmes.Star1)
filmes.Star2 = le.fit_transform(filmes.Star2)
filmes.Star3 = le.fit_transform(filmes.Star3)
filmes.Star4 = le.fit_transform(filmes.Star4)
filmes["Genre 1"] = le.fit_transform(filmes["Genre 1"])
filmes["Genre 2"] = le.fit_transform(filmes["Genre 2"])
filmes["Genre 3"] = le.fit_transform(filmes["Genre 3"])


#verificando quais variáveis são mais relevantes através dos valores de correlação
X_test = filmes[["Certificate", "Runtime", "Meta_score", "Director", "Star1", "Star2",
            "Star3", "Star4", "No_of_Votes", "Gross", "Genre 1", "Genre 2", "Genre 3"]]
print(X_test.corrwith(filmes["IMDB_Rating"]))

#o conjunto final escolhido foi o seguinte
y = filmes["IMDB_Rating"]
X = filmes[["Meta_score", "No_of_Votes", "Gross", "Runtime"]]


#dividindo os dados em conjuntos de teste e treino
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)


#etapa de modelagem
gbr = GradientBoostingRegressor(learning_rate=0.01, max_depth=3, n_estimators=500)
modelo_treinado = gbr.fit(X_train, y_train)


#as notas que o modelo retornou
pred_nota = modelo_treinado.predict(X_test)

#calculando os valores de MAE (erro médio absolute) e RMSE (erro quadrático médio)
media = mean_absolute_error(y_true=y_test, y_pred=pred_nota)
mae = mean_squared_error(y_true=y_test, y_pred=pred_nota)
rmse = math.sqrt(mae)

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")

#plotando a comparação entre os valores reais e do modelo
plt.scatter(y_test, pred_nota)
plt.xlabel("Valores Reais")
plt.ylabel("Valores Modelo")
plt.title("Real vs Modelo")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], "r--")

path_grafico = os.path.join("graficos_gerados/gradient_boosting", "resultados_modelo.png")
plt.savefig(path_grafico, dpi=500) 
plt.close()

#aplicando validação cruzada para avaliar o desempenho de um modelo
print(f"R² médio: {cross_val_score(gbr, X_train, y_train, cv=10, n_jobs=-1).mean()}")
print(f"MAE médio: {-cross_val_score(gbr, X_train, y_train, cv=10, n_jobs=-1, scoring='neg_mean_absolute_error').mean()}")
print(f"RMSE médio: {np.sqrt(-cross_val_score(gbr, X_train, y_train, cv=10, scoring='neg_mean_squared_error', n_jobs=-1)).mean()}")

#salvando o modelo já treinado em um arquivo
with open("modelagem/gradient_boosting.pkl", "wb") as f:
	pickle.dump(modelo_treinado, f)