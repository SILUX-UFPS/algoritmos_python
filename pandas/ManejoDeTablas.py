import numpy as np
import pandas as pd

a = np.array([2,3,4], dtype= np.uint32) #numpy se usa pa manejar numeros muy grandes

#las series son como una columna de una BD
s = pd.Series(np.random.randint(0,1000,5), index=["a","b","c","d","e"], name="cantidad") #index es el nombre de la fila, el index es opcional, si no toma valores de 0 a n
                                                                                        #el name es el nombre de la columna
s

d = {"one":[1,2,3,4], "tow":[4,3,2,1]}
df1 = pd.DataFrame(d)
df1

data2=[{"a":1,"b":2},{"a":5,"b":10,"c":20}] #el a,b y c se puede cambiar por cualquier cosa  y ya pareceria una tabla de una BD
df2=pd.DataFrame(data2)
df2
