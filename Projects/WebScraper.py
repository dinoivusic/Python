import requests, csv
from selenium import webdriver

def scrap(coin):
    '''Web scraping for coins and storing then into a csv file'''
    url = 'https://coinmarketcap.com/'
    res = requests.get(url)
    res.raise_for_status()
    web = webdriver.Chrome()
    web.get(url)
    assert 'coin' not in web.title
    coins = web.find_element_by_link_text(coin)
    coins.click()
    price = web.find_element_by_css_selector('#quote_price > span.h2.text-semi-bold.details-panel-item--price__value')
    coinprice = price.text
    try:
        diff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.positive_change > span')
    except:
        diff = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--header.flex-container > div.details-panel-item--price.bottom-margin-1x > span.h2.text-semi-bold.negative_change > span')
    coindiff = diff.text
    cap = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(1) > div > span:nth-child(1) > span:nth-child(1)')
    coincap = cap.text
    vol = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(2) > div > span:nth-child(1) > span:nth-child(1)')
    coinvol = vol.text
    circ = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(3) > div > span')
    coincirc = circ.text
    max = web.find_element_by_css_selector('body > div.container.main-section.padding-top-1x > div.cmc-main-content > div.cmc-main-content__main > div.details-panel.flex-container.bottom-margin-2x > div.details-panel-item--marketcap-stats.flex-container > div:nth-child(4) > div > span')
    coinmax = max.text
    web.back()
    with open("coin.csv", "w+") as coins:
        writer = csv.writer(coins)
        writer.writerow(["Coin", "Price", "Difference", "Market Cap", "Volume(24h)", "Circulating Supply", "Max supply"])
        writer.writerow([coin, coinprice, coindiff, coincap, coinvol, coincirc, coinmax])

scrap('Bitcoin')