import requests
import bs4
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(cred)

sheet3 = client.open('test scrape').worksheet('Sheet3')

req = requests.get('https://www.pesobility.com/stock')
soup = bs4.BeautifulSoup(req.text,'lxml')
code = soup.select("td > a")

for i in code:
	for x in range(len(code)):
		sheet3.update_cell(x,1,i.text)
