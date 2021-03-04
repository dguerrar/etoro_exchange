import datetime

def calculus(hashExchangeRates,dfs):
    sumSymbol=0
    sumBase=0
    # the insteresing columns are: profit (8), closed date (10)
    for index, row in dfs.iterrows(): 
        date= row['Close Date']
        pasta=row['Profit']
        
        date_time_obj = datetime.datetime.strptime(date, '%d/%m/%Y %H:%M')
        #get rates
        dayExchangeRate=hashExchangeRates[str(date_time_obj.date())]
        #print(pasta, date_time_obj.date(),dayExchangeRate )
        sumSymbol= sumSymbol + pasta
        sumBase= sumBase + pasta/dayExchangeRate
    return [sumSymbol,sumBase]

