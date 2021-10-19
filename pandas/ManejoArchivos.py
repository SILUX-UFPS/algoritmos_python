
#Archivo  https://drive.google.com/file/d/15TYUiMB6wWEv1OBRc8emqkpQXctr6meL/view?usp=sharing
import pandas as pd
data = pd.read_csv("Customer Churn Model.txt")
data.head()
subset = data[["Account Length", "Phone", "Eve Charge", "Day Calls"]] #Crear un subset con unas columnas en especifico
subset.head()
data[data["Day Mins"]>300] #Tambien se pueden hacer operaciones para filtrar
data["Total Mins"]= data["Day Mins"] + data["Night Mins"] + data["Eve Mins"] #Agregar una nueva columna siendo esta una compuesta de otras
data
