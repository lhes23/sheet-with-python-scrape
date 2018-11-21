import requests
import bs4
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('../client_secret.json',scope)
client = gspread.authorize(cred)

sheet3 = client.open('test scrape').worksheet('Sheet3')

req = requests.get('https://www.pesobility.com/stock')
soup = bs4.BeautifulSoup(req.text,'lxml')
code = soup.select("tr")


data = []
for x in code:
	td = x.find_all('td')
	#print("%s - %s - %s" % (td[0].text,td[1].text,td[2].text))
	data.append([td[0].text,td[1].text,td[2].text,td[3].text,td[4].text,td[5].text,td[6].text,td[7].text])

for i in range(len(data)):
	l = i + 1
	sheet3.insert_row(data[i],l)