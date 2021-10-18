import pandas as pd

"""
read into memory an show info from file named 'conjunto_datos_abiertos.csv'

before running python read_data_csv.py install requirements.txt

pip install requirements.txt

"""
def read_csv(location: str = "conjunto_datos_abiertos.csv"):
    result = pd.read_csv(location)
    print(result.info())


read_csv()