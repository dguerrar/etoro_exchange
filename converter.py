import exchange_api as api
import readXlsx as reader
import calculations as calculations
import feeds as feeds


def convert(startDate, endDate, currency, baseCurrency, eToroXlxsFile):
    #get exchange rates from internet

    hashExchangeRates=api.getExchangeRates(startDate, endDate,currency,baseCurrency);

    #for day,rate in hashExchangeRates.items():
    #    print (day + " : "+ str(rate))

    #read xls file from my etoro account

    dfs= reader.readTransactionXlxs(eToroXlxsFile, 'Closed Positions')


    [sumSymbol,sumBase]=calculations.calculus(hashExchangeRates,dfs)
    print ("****Results****")
    print ("Lost/Profit :" + str(sumSymbol) +" " +currency)
    print ("Lost/Profit :" + str(sumBase) +" " + baseCurrency)

    dfsFeeds= reader.readTransactionXlxs(eToroXlxsFile, 'Transactions Report')

    [suma1, suma2]=feeds.processFeeds(hashExchangeRates,dfsFeeds)

    print ("****Results feeds****")
    print ("Feeds :" + str(suma1) +" " +currency)
    print ("Feeds :" + str(suma2) +" " + baseCurrency)
