import requests
from nltk.featstruct import retract_bindings

API_KEY = 'aLOkMcHbtZ0LuDLoDKswAWT8a9CDrSzZCa0FLYSD'

URL = 'https://api.open.fec.gov/v1/candidate/P80000722/'

params = {'api_key':API_KEY}


def get_data():
    response = requests.get(URL, params=params)
    return response.json()