import requests, csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://coinmarketcap.com/'
res = requests.get(url)
res.raise_for_status()
web = webdriver.Chrome()
web.get('https://coinmarketcap.com/')
assert 'coin' not in web.title
btc = web.find_element_by_link_text('Bitcoin')
btc.click()
btcprice = web.find_element_by_css_selector('#quote_price > span.h2.text-semi-bold.details-panel-item--price__value')
bitcoinprice = btcprice.text
with open("coin.csv", "w+") as coins:
    fieldnames = ["Coin", "Price"]
    writer = csv.writer(coins)
    writer.writerow(["Coin", "Price"])
    writer.writerow(["Bitcoin", bitcoinprice])

