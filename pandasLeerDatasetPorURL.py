import pandas as pd
#Leer datos desde URL
medals_url = "http://winterolympicsmedals.com/medals.csv"
medals_data = pd.read_csv(medals_url)
medals_data.shape #Ver cantidad de filas y columnas
medals_data.info() #Ver informacion de las columnas
data.describe(include="all") #informacion descriptiva de la tabla
data.dtypes #tipos de datos por columna
data[["sex","age"]][0:5] #para sacer algunas columnas en especifico, y el segundo [] pa la cantidad
data.loc[0:6,"name":"age"] #similar al anterior, el : es pa especificar un rango
data.iloc[0:6,0:4] #Lo mismo de la anterior pero en vez del nombre de la columna usa el numero
data["body"].isnull().count() #contar los nulos
data.body.isna().value_counts() #lo mismo de la anterior pero por tipo de datos
data.fillna(0) #para completar donde este nulo por 0
data["body"].fillna(data.body.mean()) #Rellenar con la media valores nulos
data["age"].fillna(method="backfill") #Rellenar con el anterior, si en vez de backfill se pone ffill es el siguiente
data.drop(columns="name") #Borrar una columna"
dummy_sex = pd.get_dummies(data["sex"], prefix="sex", drop_first=True) #añade un prefijo al nombre del atributo, es para transformarlo a numerico
                                                            #El drop_first es para eliminar la primera columna, ya que se puede deducir de las demas
dummy_sex#Para luego borrar en la columna de data el campo sex y agregar esta, y seria:
pd.concat([data, dummy_sex], axis=1) 
