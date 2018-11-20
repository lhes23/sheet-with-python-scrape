import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import bs4
import lxml

scope =['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
client = gspread.authorize(cred)

sheet = client.open('test scrape').sheet1
sheet2 = client.open('test scrape').worksheet("Sheet2")

#result = sheet.get_all_records()
#result = sheet.cell(2,3).value
#data = ["I","am","inserting","a","row"]
#result = sheet.insert_row(data,3)

result = sheet2.col_values(1)

for x in range(len(result)-1):
	l = x + 1
	data = sheet2.cell(l,1).value

	res = requests.get(data)
	soup = bs4.BeautifulSoup(res.text,'lxml')
	title = soup.select('title')

	for i in title:
		the_title = i.text
		sheet2.update_cell(l,2,the_title)
