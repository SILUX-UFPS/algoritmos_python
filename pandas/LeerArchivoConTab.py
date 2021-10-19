
#https://drive.google.com/drive/folders/17jL1pSjpI8lUTcXackZxOr7ffYi5mCox?usp=sharing Link de acceso al dataset titanic3
import pandas as pd

data = pd.read_csv('C:/Users/RYZEN/Documents/Cods/titanic3.csv')
data.head(10)
#para leer un archivo csv que el separador sea un tab y no una , se hace lo siguiente:
data2 = pd.read_csv('C:/Users/RYZEN/Documents/Cods/Tab Customer Churn Model.txt', sep="\t")
data2.head(10)
