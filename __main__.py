import converter as conv
import sys

print("****Starting process****")
#params from command line must be in the following format
#startDate= "2020-01-01"
#endDate="2020-12-31"
#currency="USD"
#base="EUR"
#fileName="d:\pampol\phyton_test\etoro_history_exchange\etoro_exchange\eToroAccountStatement.xlsx";

#check params from command line

startDate= sys.argv[1]
endDate=sys.argv[2]
currency=sys.argv[3]
base=sys.argv[4]
fileName=sys.argv[5]


conv.convert(startDate, endDate, currency, base, fileName)
print("****Finishing process****") 