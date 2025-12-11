import yfinance as yf
import json
import pandas as pd

import datetime
import time
import numpy as np


class Stock():
    def getTicker(query):
        search = yf.Search(query=query)
        data = search.quotes
        result = []
        for i in data:
            result.append({"symbol" : i.get('symbol'),
                            "longname" : i.get("longname") or i.get("shortname"),
                            "industry" : i.get('industry')
                            })
        return result
    def getBalanceSheet(ticker):
        stock = yf.Ticker(ticker)
        df = stock.balance_sheet.copy()

# Convert column names to datetime
        df.columns = pd.to_datetime(df.columns, errors='ignore')

# Convert to string dates
        df.columns = df.columns.strftime('%Y-%m-%d')
        json_data = df.T.to_json(orient='index')
        return json_data

        
        
    #.to_json()

