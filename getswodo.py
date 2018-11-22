import requests
import bs4


req = requests.get('https://www.getwsodo.com/requests/?pagenum=10')
soup = bs4.BeautifulSoup(req.text,'html.parser')

div = soup.find('div',{'id':'gv-item-reviewed'})

tbody = div.find('tbody')

data = []
for tr in tbody.find_all('tr'):
	course = tr.find_all('td')[0].text.strip()
	td = tr.find_all('td')[1]
	link = td.find_all('a')[0].get('href')
	vote = tr.find_all('td')[2].text.strip()
	data.append([course,link,vote])

print(data)