import pandas as pd

"""
show list of columns of the file csv with boolean attribute
True if exists values None otherwise shows False
"""

def read_csv_columns_none(location: str = "conjunto_datos_abiertos.csv"):
    result = pd.read_csv(location)
    print(result.isnull().any())


read_csv_columns_none()