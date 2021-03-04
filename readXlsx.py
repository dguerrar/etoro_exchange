import pandas as pd

#read the entire xlxs into a dataframe
def readTransactionXlxs(file, sheetName):
    dfs = pd.read_excel(file,sheetName)
    return dfs;


