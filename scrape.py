import requests
import bs4
import lxml

res = requests.get('https://lesterreandino.com')
soup = bs4.BeautifulSoup(res.text,'lxml')
title = soup.select('title')

for x in title:
	print(x.text)