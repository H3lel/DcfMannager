import yfinance as yf
import json

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
    
        
