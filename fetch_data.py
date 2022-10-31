import requests
import json
from endpoint_URL import URL

def fetch():
    response = requests.get(URL)
    
    if response.status_code == 200:
        data_set = response.json()
        countries = []
        for data in data_set['Countries']:
            countries.append([
                 data['Date'],
                 data['Country'],
                 data['TotalConfirmed'], 
                 data['TotalRecovered'],
                 data['TotalDeaths']
                ])
        return countries
    return f'OOPS!! An error with status code {response.status_code} occured'
