# -*- coding: utf-8 -*-

# Reto 03. Ante usted tiene datos de salario y posición laboral, donde los que se percibe
# depende de la posición laboral. Primero, deberá hacer uso de una regresión
# lineal, y en un segundo paso, hacer uso de una no lineal para poder explicar las ventajas de pensar más allá en términos
# de una no relación lineal ¡Éxito!

# Carguemos las librerías necesarias

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("Current Working Directory " , os.getcwd())
os.chdir("C:/Users/Pelu/OneDrive - UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO/cosas de Jaff Koalita/Bedu/ML/Sesion 04/Reto03")


# 1. Importe el dataset. Para este ejercicio no deberá partir entre dataset de entrenamiento
# y prueba


# 2. Haga una regresión lineal con los datos x e y ajustados.


# 2.5 Visualice su regresión lineal



# 3. Desarrolle su modelo de regreisón polinomial (nota: use from sklearn.preprocessing import PolynomialFeatures
# despues use PolynomialFeatures con el argumento de degree experimentando distintos grados
#, para ello puede ir graficando su regreisón estimada, hasta llegar a la que haga
# mejor ajuste visualmente. Tambien use su_regresion.fit_transform('su variable x'))


# 4. Visualice su regresión no lineal



# 5. Genere una predicción con la regresion lineal para la posición laboral 12 con 
# lin_reg.predict, y ahora genere una con la no lineal (CONSEJO SALVA VIDAS: 
# se hace con la misma base de la regreison lineal pero agregue .suRegresionNoLineal.fit_transform)



# 6. BONUS: Visualice su regresión no lineal con una suavización de la recta

