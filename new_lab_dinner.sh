#!/usr/bin/env bash

fname=$(date +"%Y_%m_%d")_lab_dinner.html
cp scripts/lab_dinner_template.html $fname
foodler=$(ls -t *html | grep -i foodler | head -n 1)
todaydate=$(python scripts/lab_dinner.py "$foodler" todaydate)
orderdate=$(python scripts/lab_dinner.py "$foodler" orderdate)
price=$(python scripts/lab_dinner.py "$foodler" price)

sed -i '' "s,todaysdate,$todaydate," $fname 
sed -i '' "s,dateofpurchase,$orderdate," $fname 
sed -i '' "s/price/$price/" $fname 

echo $fname
open $fname
echo $foodler
open $foodler
