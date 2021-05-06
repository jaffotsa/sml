# -*- coding: utf-8 -*-

# Reto 01. Entrena un modelo de regresión lineal con los datos proporcionados. Usted
# debe realizar una proyección con una regresión que defina al precio como una función dependiente
# de los pies cuadrados (el espacio en una vivienda). Es libre de desarrollar EDA para entender
# sus datos antes de realizar el ejercicio.

# 1. Importe las librerías necesarias (Pandas, matplotlib, scikit-learn numpy y os si usa spyder u otra IDE
# que no sea Jupyter)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sklearn


%matplotlib inlinepath
np.set_printoptions(threshold=np.nan)


# 2. Haga el data wrangling necesario. Recuerde. DEBE FIJAR COMO VARIABLE INDEPENDIENTE A 
# sqft_living Y COMO DEPENDIENTE A price. Como pista, debe convertir a arrat de numpy 
# sus variables y hacerle un reshape de (-1, 1) a sqft_living



# Separe en conjunto entrenamiento y en conjunto de prueba con Scikit Learn. (Pista:
# usa la vieja confiable de xtrain, xtest, ytrain, ytest = ... con la infalibre sublibrería
# from from sklearn.model_selection import train_test_split )


# Ajuste el modelo de regresión en los datos de entrenamiento con el siguiente template
# from sklearn.linear_model import LinearRegression 
# regressor = LinearRegression()
# regressor.fit('tu eje de las x de training', 'tu eje de las y de training')


# Genera tu predicción con regressor.predict



# Visualiza tus resultados con matplotlib


# Haz la prueba con el conjunto de prueba y visualiza

