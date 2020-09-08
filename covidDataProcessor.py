import pandas as pd

def getRecordByCountry(data_confirmed, data_deaths, countryName):
    data_confirmed_filtered = data_confirmed[data_confirmed['Country/Region'] == countryName]
    data_deaths_filtered = data_deaths[data_deaths['Country/Region'] == countryName]
    return data_confirmed_filtered, data_deaths_filtered

def removeUnnecesaryColumns(data_confirmed, data_deaths):
    del data_confirmed['Lat']
    del data_confirmed['Long']
    del data_confirmed['Province/State']

    del data_deaths['Lat']
    del data_deaths['Long']
    del data_deaths['Province/State']
    
    return data_confirmed, data_deaths

def transposeData(data_confirmed, data_deaths):
    tmp_confirmed, tmp_death =  data_confirmed.rename(columns={'Country/Region':'Date'}).T, data_deaths.rename(columns={'Country/Region':'Date'}).T
    tmp_confirmed.columns, tmp_death.columns = tmp_confirmed.iloc[0], tmp_death.iloc[0]
    tmp_confirmed, tmp_death = tmp_confirmed.iloc[1:], tmp_death.iloc[1:]
    tmp_confirmed.rename(columns={tmp_confirmed.columns[0]:'Total'}, inplace=True)
    tmp_death.rename(columns={tmp_death.columns[0]:'Total'}, inplace=True)

    tmp_confirmed.index = pd.to_datetime(tmp_confirmed.index.astype(str), format='%m/%d/%y')
    tmp_death.index = pd.to_datetime(tmp_death.index.astype(str), format='%m/%d/%y')

    return tmp_confirmed, tmp_death
    
def getRecordsAfterDate(confirmed, deaths, date):
    return confirmed[confirmed.index >= date], deaths[deaths.index >= date]