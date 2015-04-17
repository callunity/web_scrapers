from lxml import html
import requests
import re

page = requests.get('http://www.bulkbarn.ca/en-ca/promotions.html?p=ontario')
tree = html.fromstring(page.text)

all_items = tree.xpath('//h3[@class="name"]/text()')
all_prices = tree.xpath('//span[@class="priceLB"]/text()')

almonds = []
prices = []

for i in range(len(all_items)):
  search_almonds = re.search( r'([Aa])lmond\w+', all_items[i])
  if search_almonds:
    almonds.append(all_items[i])
    prices.append(all_prices[i])
 
if almonds[0]:
  for i in range(len(almonds)):
    print almonds[i], ': $', prices[i]
else:
  print "No almonds this week." 
