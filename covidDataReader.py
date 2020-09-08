import pandas as pd

def read():
    repo_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/'

    confirmed_url = repo_url + 'time_series_covid19_confirmed_global.csv'
    deaths_url = repo_url + 'time_series_covid19_deaths_global.csv'
    
    data_confirmed = pd.read_csv(confirmed_url)
    data_deaths = pd.read_csv(deaths_url)
    
    return data_confirmed,data_deaths