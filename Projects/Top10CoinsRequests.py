import csv, requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
url = 'https://coinmarketcap.com/'

res = requests.get(url)
print(res.status_code)

coinList = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

lists = requests.get(coinList)
params = {
  'start':'1',
  'limit':'10'
}
headers = {'Accepts': 'application/json', 'Accept-Encoding': 'deflate, gzip', 'X-CMC_PRO_API_KEY': '9bfc5aee-cd89-463f-a805-62ca8115b353'}
session = requests.Session()
session.headers.update(headers)

try:
    response = session.get(coinList, params=params)
    data = response.json()
    print(json.dumps(data, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as err:
    print(err)

onePrice = data['data'][0]['quote']['USD']['price']
oneName = data['data'][0]['name']
oneChange24 = data['data'][0]['quote']['USD']['percent_change_24h']
oneCap = data['data'][0]['quote']['USD']['market_cap']

twoPrice = data['data'][1]['quote']['USD']['price']
twoName = data['data'][1]['name']
twoChange24 = data['data'][1]['quote']['USD']['percent_change_24h']
twoCap = data['data'][1]['quote']['USD']['market_cap']

threePrice = data['data'][2]['quote']['USD']['price']
threeName = data['data'][2]['name']
threeChange24 = data['data'][2]['quote']['USD']['percent_change_24h']
threeCap = data['data'][2]['quote']['USD']['market_cap']

fourPrice = data['data'][3]['quote']['USD']['price']
fourName = data['data'][3]['name']
fourChange24 = data['data'][3]['quote']['USD']['percent_change_24h']
fourCap = data['data'][3]['quote']['USD']['market_cap']

fivePrice = data['data'][4]['quote']['USD']['price']
fiveName = data['data'][4]['name']
fiveChange24 = data['data'][4]['quote']['USD']['percent_change_24h']
fiveCap = data['data'][4]['quote']['USD']['market_cap']

sixPrice = data['data'][5]['quote']['USD']['price']
sixName = data['data'][5]['name']
sixChange24 = data['data'][5]['quote']['USD']['percent_change_24h']
sixCap = data['data'][5]['quote']['USD']['market_cap']

sevenPrice = data['data'][6]['quote']['USD']['price']
sevenName = data['data'][6]['name']
sevenChange24 = data['data'][6]['quote']['USD']['percent_change_24h']
sevenCap = data['data'][6]['quote']['USD']['market_cap']

eightPrice = data['data'][7]['quote']['USD']['price']
eightName = data['data'][7]['name']
eightChange24 = data['data'][7]['quote']['USD']['percent_change_24h']
eightCap = data['data'][7]['quote']['USD']['market_cap']

ninePrice = data['data'][8]['quote']['USD']['price']
nineName = data['data'][8]['name']
nineChange24 = data['data'][8]['quote']['USD']['percent_change_24h']
nineCap = data['data'][8]['quote']['USD']['market_cap']

tenPrice = data['data'][9]['quote']['USD']['price']
tenName = data['data'][9]['name']
tenChange24 = data['data'][9]['quote']['USD']['percent_change_24h']
tenCap = data['data'][9]['quote']['USD']['market_cap']

with open ('coinRequest.csv', 'w+') as coins:
    writer = csv.writer(coins)
    writer.writerow(['Coin', 'Price', 'Change in 24h', 'Market Cap'])
    writer.writerow([oneName, onePrice, oneChange24,oneCap])
    writer.writerow([twoName, twoPrice, twoChange24, twoCap])
    writer.writerow([threeName, threePrice, threeChange24, threeCap])
    writer.writerow([fourName, fourPrice, fourChange24, fourCap])
    writer.writerow([fiveName, fivePrice, fiveChange24, fiveCap])
    writer.writerow([sixName, sixPrice, sixChange24, sixCap])
    writer.writerow([sevenName, sevenPrice, sevenChange24, sevenCap])
    writer.writerow([eightName, eightPrice, eightChange24, eightCap])
    writer.writerow([nineName, ninePrice, nineChange24, nineCap])
    writer.writerow([tenName, tenPrice, tenChange24, tenCap])
