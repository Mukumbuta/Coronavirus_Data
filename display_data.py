import pandas as pd
from fetch_data import fetch


def display(fetch):
    covid_data = fetch()
    data_frame = pd.DataFrame(
            data=covid_data, 
            columns=['Date', 'Country', 'Total Confirmed', 'Total Recovered', 'Total Deaths']
        ) 

    print(data_frame.head(20))
    return data_frame

display(fetch)