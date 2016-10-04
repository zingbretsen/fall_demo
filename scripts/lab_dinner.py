#!/bin/env python
from bs4 import BeautifulSoup as bs
import json
import sys
import time


with open(sys.argv[1], 'r') as foodler:
    soup = bs(foodler.read(), 'lxml')

js = soup.script.text
dec = json.JSONDecoder()
js_decoded = dec.decode(js)
price = js_decoded['price']
orderDate = js_decoded['orderDate'].split('T')[0]
y = orderDate.split('-')[0]
m = orderDate.split('-')[1]
d = orderDate.split('-')[2]

try:
    if sys.argv[2] == "price":
        print(price)
    if sys.argv[2] == "orderdate":
        print('{}/{}/{}'.format(m, d, y))
    if sys.argv[2] == "todaydate":
        print(time.strftime('%m/%d/%y'))
except:
    pass
