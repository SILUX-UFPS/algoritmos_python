import json
from fuzzywuzzy import process

"""
open example_data.json and use json.load() to return list of str
"""
def get_car_models_name():
    with open("example_data.json", encoding="utf-8", mode="r") as data:
        car_models = json.load(data)
    car_name_models = [car_model["Name"] for car_model in car_models]
    return car_name_models

"""
use the metric Levenshtein Distance 
to calculate the similarity of two text strings
more info https://jairoandres.com/string-matching-a-lo-pythonico/

before running python search.py isntall requirements.txt

pip install -r requirements.txt
"""
def search_model_car(model_name: str):
    car_models_name = get_car_models_name()
    return process.extractOne(model_name, car_models_name)


print(search_model_car("CoNcurOs"))