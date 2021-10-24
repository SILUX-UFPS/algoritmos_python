import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

df.isna().count()

condiciones = [(df.quality > 5),
               (df.quality == 5),
               (df.quality < 5),
               ]
elecciones = np.array(('bueno', 'regular', 'malo'))
df["Categoría"] = np.select(condiciones, elecciones, -1)

df.head(50)

df = df.drop(['quality'], axis=1)

df.head(3)

df['Categoría'].count()

df['Categoría'].value_counts().plot(kind= "bar", title="Categorias")

df.plot(kind="bar", x="Categoría")
df.corr()

import seaborn as sns

# Representación del mapa de calor
sns.heatmap(df.corr(), center=0, cmap='Blues_r', fmt='.3f')

