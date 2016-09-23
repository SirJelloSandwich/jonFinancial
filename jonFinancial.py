

#!/usr/bin/python
import pandas as pd
import numpy as np
import urllib2 as url
import requests
import json

myTradeIds = []

 #API uses pagination - https://docs.gdax.com/#pagination ##
response = url.urlopen('https://api.gdax.com/products/ETH-USD/trades')
headers = response.info().headers

for thing in headers:
    if 'cb-after:' in thing:
        print thing

myJson = json.load(response)
file = open('jonsData', 'w')
for thing in myJson:

    file.write(str(thing['trade_id'])+"\n")
file.close
