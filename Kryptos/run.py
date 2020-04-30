from kryptos import app
import requests
import csv
import json
from datetime import datetime
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

#Btc
session = requests.Session()
coinBtc = 'http://api.coincap.io/v2/assets/bitcoin'
try:
    response = session.get(coinBtc)
    data = response.json()
    print(json.dumps(data, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as err:
    print(err)

btcPrice = float(data['data']['priceUsd'])
btcTime = data['timestamp']
dt_object = datetime.fromtimestamp(btcTime / 1000)
usdVolume = data['data']['volumeUsd24Hr']
params = [dt_object, float(btcPrice), float(btcPrice),
            float(btcPrice), btcPrice, usdVolume]

with open('kryptos/Bitcoins.csv', 'a') as btc:
    writer = csv.writer(btc)
    writer.writerow(params)

#Eth
session = requests.Session()
coinEth = 'http://api.coincap.io/v2/assets/ethereum'
try:
    response = session.get(coinEth)
    data = response.json()
    print(json.dumps(data, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as err:
    print(err)

ethPrice = float(data['data']['priceUsd'])
ethTime = data['timestamp']
dt_object = datetime.fromtimestamp(btcTime / 1000)
usdVolume = data['data']['volumeUsd24Hr']
params = [dt_object, float(ethPrice), float(ethPrice),
            float(ethPrice), ethPrice, usdVolume]

with open('kryptos/ether.csv', 'a') as eth:
    writer = csv.writer(eth)
    writer.writerow(params)

#Neo
session = requests.Session()
coinNeo = 'http://api.coincap.io/v2/assets/neo'
try:
    response = session.get(coinNeo)
    data = response.json()
    print(json.dumps(data, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as err:
    print(err)

neoPrice = float(data['data']['priceUsd'])
neoTime = data['timestamp']
dt_object = datetime.fromtimestamp(btcTime / 1000)
usdVolume = data['data']['volumeUsd24Hr']
params = [dt_object, float(neoPrice), float(neoPrice),
            float(neoPrice), neoPrice, usdVolume]

with open('kryptos/neo.csv', 'a') as neo:
    writer = csv.writer(neo)
    writer.writerow(params)

#Ltc
session = requests.Session()
coinLtc = 'http://api.coincap.io/v2/assets/litecoin'
try:
    response = session.get(coinLtc)
    data = response.json()
    print(json.dumps(data, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as err:
    print(err)

ltcPrice = float(data['data']['priceUsd'])
ltcTime = data['timestamp']
dt_object = datetime.fromtimestamp(btcTime / 1000)
usdVolume = data['data']['volumeUsd24Hr']
params = [dt_object, float(ltcPrice), float(ltcPrice),
            float(ltcPrice), ltcPrice, usdVolume]

with open('kryptos/litecoin.csv', 'a') as ltc:
    writer = csv.writer(ltc)
    writer.writerow(params)



if __name__ == '__main__':
    app.run(debug=True, port=3000)
