import pandas as pd
import requests, json


def update_data():
    """
    Update data from the csv file to the database
    """
    url = 'https://opendata.ecdc.europa.eu/covid19/casedistribution/json/'
    resp = requests.get(url)
    data = json.loads(resp.text)
    records = data['records']
    df = pd.DataFrame(records)
    df = df.rename(columns={'dateRep': 'date'})[['date', 'day', 'month', 'year', 'cases', 'deaths', 'countriesAndTerritories', 'geoId', 'countryterritoryCode', 'popData2019', 'continentExp']]
    df.to_csv('covid_data.csv', index=False)
