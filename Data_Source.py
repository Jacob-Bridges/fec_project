import requests
from nltk.featstruct import retract_bindings

API_KEY = '' #API Key removed for security purposes

URL = 'https://api.open.fec.gov/v1/candidate/P80000722/'

params = {'api_key':API_KEY}


def get_data():
    response = requests.get(URL, params=params)
    return response.json()
