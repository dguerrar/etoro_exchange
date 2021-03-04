import readXlsx as reader
import datetime as datetime

def processFeeds (hashExchangeRates,df):
    sumSymbol=0
    sumBase=0
    for index, row in df.iterrows(): 
        date= row['Date']
        pasta=row['Amount']
        type=row['Type']

        if (type=="Rollover Fee"):
            date_time_obj = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            #get rates
            dayExchangeRate=hashExchangeRates[str(date_time_obj.date())]
            #print(pasta, date_time_obj.date(),dayExchangeRate )
            sumSymbol= sumSymbol + pasta
            sumBase= sumBase + pasta/dayExchangeRate
    return [sumSymbol,sumBase]
