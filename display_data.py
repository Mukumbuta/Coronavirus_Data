import pandas as pd
from fetch_data import fetch
from create_csv import create_csv


def display(fetch):
    covid_data = fetch()
    data_frame = pd.DataFrame(
            data=covid_data, 
            columns=['Date', 'Country', 'Total Confirmed', 'Total Recovered', 'Total Deaths']
          ) 
    create_csv(data_frame)
    print(data_frame.head(20))
    
    return data_frame


display(fetch)