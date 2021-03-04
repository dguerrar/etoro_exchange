import requests
import json

#https://exchangerate.host/#/docs

def getExchangeRates(startDate, endDate,currency,base):
    hashExchangeDates={}
    urlapi='https://api.exchangerate.host/timeseries?start_date={0}&end_date={1}&symbols={2}&base={3}'.format(startDate, endDate,currency,base)
    
    resp = requests.get(urlapi)
    if resp.status_code == 200:

        #print('{}'.format())
        jsonDataExchange=resp.json();
        #print('{}'.format(jsonDataExchange['rates']))
        #create empty dictionay
        
        for dayRate,rate in jsonDataExchange['rates'].items():
            hashExchangeDates[dayRate] =rate['USD']

    else:
        raise IOError('GET  {} {}'.format(urlapi,resp.status_code))

    return hashExchangeDates

