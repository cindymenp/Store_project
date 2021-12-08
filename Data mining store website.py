import pandas as pd
import requests
from  bs4 import BeautifulSoup

url = 'https://www.hm.com/om/store-locator/netherlands/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
paragraph_division = soup.findAll(attrs = {'class' : 'content'})
stores = paragraph_division[0].findAll(attrs = {'class': 'store-dropdown'})

def parseOpeningHour(line):
    tds = line.findAll('td')
    day = tds[0].text.strip()
    hours = tds[1].text.strip().split(' - ')
            
    return { 'day': day, 'opensAt': hours[0], 'closesAt': hours[1] }

def parseException(line):
    tds = line.findAll('td')
    date = tds[0].text.strip()
    exception = tds[1].text.strip()
    
    return { 'date': date, 'exception': exception }

def parseStore(store):
    exceptions = store.find(attrs = { 'class': 'opening-hours-exceptions' })
    
    return {
        'name': store.find('h3').text,
        'address': store.find('p').text,
        'openingHours': [
            parseOpeningHour(line)
            for line in store.find(attrs = { 'class': 'opening-hours' }).findAll('tr')
        ],
        'exceptions': [] if exceptions == None else [parseException(line) for line in exceptions.findAll('tr')]
    }
    
storeTable = [parseStore(store) for store in stores]

text_mining = paragraph_division[0].text

store_mining = paragraph_division[-1].text

soup.find(attrs={'class': 'title is-4 is-size-5-touch'}).text.replace('\n'," ")

store_information =  pd.DataFrame(storeTable, columns = ['name', 'address'])

df.to_csv("H&M.csv")  

"Start code"

print(soup)
print(paragraph_division)
print(stores)
print(storeTable)
print(text_mining)
print(store_mining)
print(store_information)
