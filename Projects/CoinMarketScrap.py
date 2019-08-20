import requests, csv
from selenium import webdriver

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
try:
    btcDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.positive_change > span')
except:
    btcDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.negative_change > span')
btcdiff = btcDiff.text
btcCap = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(1) > div > span:nth-child(1) > span:nth-child(1)')
btccap = btcCap.text
btcVolume = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(2) > div > span:nth-child(1) > span:nth-child(1)')
btcvol = btcVolume.text
btcCirc = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(3) > div > span')
btccirc = btcCirc.text
btcMax = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(4) > div > span')
btcmax = btcMax.text
web.back()
eth = web.find_element_by_link_text('Ethereum')
eth.click()
ethprice = web.find_element_by_css_selector('#quote_price > span.h2.text-semi-bold.details-panel-item--price__value')
etherprice = ethprice.text
try:
    ethDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.positive_change > span')
except:
    ethDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.negative_change > span')
ethdiff = ethDiff.text
ethCap = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(1) > div > span:nth-child(1) > span:nth-child(1)')
ethcap = ethCap.text
ethVolume = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(2) > div > span:nth-child(1) > span:nth-child(1)')
ethvol = ethVolume.text
ethCirc = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(3) > div > span')
ethcirc = ethCirc.text
web.back()
xrp = web.find_element_by_link_text('XRP')
xrp.click()
xrpPrice = web.find_element_by_css_selector('#quote_price > span.h2.text-semi-bold.details-panel-item--price__value')
xrpprice = xrpPrice.text
try:
    xrpDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.positive_change > span')
except:
    xrpDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.negative_change > span')
xrpdiff = xrpDiff.text
xrpCap = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(1) > div > span:nth-child(1) > span:nth-child(1)')
xrpcap = xrpCap.text
xrpVolume = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(2) > div > span:nth-child(1) > span:nth-child(1)')
xrpvol = xrpVolume.text
xrpCirc = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(3) > div > span')
xrpcirc = xrpCirc.text
xrpMax = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(4) > div > span')
xrpmax = xrpMax.text
web.back()
bcc = web.find_element_by_link_text('Bitcoin Cash')
bcc.click()
bccPrice = web.find_element_by_css_selector('#quote_price > span.h2.text-semi-bold.details-panel-item--price__value')
bccprice = bccPrice.text
try:
    bccDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.positive_change > span')
except:
    bccDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.negative_change > span')
bccdiff = bccDiff.text
bccCap = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(1) > div > span:nth-child(1) > span:nth-child(1)')
bcccap = bccCap.text
bccVolume = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(2) > div > span:nth-child(1) > span:nth-child(1)')
bccvol = bccVolume.text
bccCirc = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(3) > div > span')
bcccirc = bccCirc.text
bccMax = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(4) > div > span')
bccmax = bccMax.text
web.back()
ltc = web.find_element_by_link_text('Litecoin')
ltc.click()
ltcPrice = web.find_element_by_css_selector('#quote_price > span.h2.text-semi-bold.details-panel-item--price__value')
ltcprice = ltcPrice.text
try:
    ltcDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.positive_change > span')
except:
    ltcDiff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.negative_change > span')
ltcdiff = ltcDiff.text
ltcCap = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(1) > div > span:nth-child(1) > span:nth-child(1)')
ltccap = ltcCap.text
ltcVolume = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(2) > div > span:nth-child(1) > span:nth-child(1)')
ltcvol = ltcVolume.text
ltcCirc = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(3) > div > span')
ltccirc = ltcCirc.text
ltcMax = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(4) > div > span')
ltcmax = ltcMax.text
web.back()
with open("coin.csv", "w+") as coins:
    writer = csv.writer(coins)
    writer.writerow(["Coin", "Price", "Difference", "Market Cap", "Volume(24h)", "Circulating Supply", "Max supply"])
    writer.writerow(["Bitcoin", bitcoinprice, btcdiff, btccap, btcvol, btccirc, btcmax])
    writer.writerow(["Ethereum", etherprice, ethdiff, ethcap, ethvol, ethcirc])
    writer.writerow(["XRP", xrpprice, xrpdiff, xrpcap, xrpvol, xrpcirc, xrpmax])
    writer.writerow(['Bitcoin Cash', bccprice, bccdiff, bcccap, bccvol, bcccirc, bccmax])
    writer.writerow(["Litecoin", ltcprice, ltcdiff, ltccap, ltcvol, ltccirc, ltcmax])
