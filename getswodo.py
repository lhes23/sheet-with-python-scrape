import requests
import bs4
import csv
import os

# for Request

# Initial data array
data = []


# Scrape the site and store it into the data
def getswodo_request(url):
	req = requests.get(url)
	soup = bs4.BeautifulSoup(req.text,'html.parser')
	div = soup.find('div',{'id':'gv-item-reviewed'})
	tbody = div.find('tbody')
	
	for tr in tbody.find_all('tr'):
		course = tr.find_all('td')[0].text.strip()
		td = tr.find_all('td')[1]
		link = td.find_all('a')[0].get('href')
		vote = tr.find_all('td')[2].text.strip()
		data.append([course,link,vote])
	return data

# Write to the CSV File
def writeToFile(data):
	with open('request.csv','w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(data)
	writeFile.close()
	print('Perfectly DONE!')



#url = input('what is the url?') 
#url = 'https://www.getwsodo.com/requests/?pagenum=4'
#getswodo_request(url)

links = [
	"https://www.getwsodo.com/requests/",
	"https://www.getwsodo.com/requests/?pagenum=2",
	"https://www.getwsodo.com/requests/?pagenum=3",
	"https://www.getwsodo.com/requests/?pagenum=4",
	"https://www.getwsodo.com/requests/?pagenum=5",
	"https://www.getwsodo.com/requests/?pagenum=6",
	"https://www.getwsodo.com/requests/?pagenum=7",
	"https://www.getwsodo.com/requests/?pagenum=8",
	"https://www.getwsodo.com/requests/?pagenum=9",
	"https://www.getwsodo.com/requests/?pagenum=10",
]

for l in links:
	data = getswodo_request(l)
	writeToFile(data)
