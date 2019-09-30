#Webscrapping for Exchange rates
#Fetching the webpage
import requests
from bs4 import BeautifulSoup
page =requests.get('https://www.bcn.gob.ni', verify = False)
print(page)

#Creating the BS object
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
# get the exchange rate
repo = soup.find(class_="indicadores one").text
repo
import re
#Regex to obtain the exchange rate as a float variable
tdc = float(re.findall('[0-9]{2}\.[0-9]+',repo)[0])
tdc