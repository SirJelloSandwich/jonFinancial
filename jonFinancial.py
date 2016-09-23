

#!/usr/bin/python
import pandas as pd
import numpy as np
import urllib2 as url
import requests
import json

myTradeIds = []

 #API uses pagination - https://docs.gdax.com/#pagination ##
response = url.urlopen('https://api.gdax.com/products/ETH-USD/trades')

myJson = json.load(response)
file = open('jonsData', 'w')
for thing in myJson:

    myTradeIds.append(thing['trade_id'])
    file.write(str(thing['trade_id'])+"\n")
file.close
