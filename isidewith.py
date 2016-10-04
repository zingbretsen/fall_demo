#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
from sys import version_info
try:
    from urllib2 import urlopen
except ImportError as e:
    from urllib.request import urlopen

isidewith = urlopen('https://www.isidewith.com/polls').read()
if version_info.major == 3:
    parser = 'html.parser'
else:
    parser = 'lxml'
isidewith_parsed = bs(isidewith, parser)

polls = isidewith_parsed.select('.poll')
polls_extracted = []

for p in polls:
    name     = p.select('a')[0].get('title')
    question = p.select('.question')[0].text
    yes      = p.select('.yes')[0].text
    no       = p.select('.no')[0].text
    count    = p.select('.count')[0].text
    polls_extracted.append(';'.join([name, question, yes, no, count]))

with open('/tmp/polls_scraped.csv', 'w') as f:
    f.write(str('\n'.join(polls_extracted).encode('utf8')))

