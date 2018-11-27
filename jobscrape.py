import requests
from bs4 import BeautifulSoup
import csv
import os


link = ["https://www.onlinejobs.ph/jobseekers/jobsearch/30"]
data = []

def scrapeSite(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	section = soup.find("section",{'class':'bg-lwhite'})
	div = section.find('div',{'class':'col-md-7'})

	a = div.find_all('div',{'class':'jobs-box'})
	for job in a:
		title = job.find_all('p')[0].text.strip()
		category = job.find_all('p')[1].text.strip()
		salary = job.find_all('p')[2].text.strip()
		details = job.find_all('p')[4].text.strip()
		data.append([title,category,salary,details])
	print(data)


# def writeToFile(data):
# 	with open('jobs.csv','w') as writeFile:
# 		writer = csv.writer(writeFile)
# 		writer.writerows(data)
# 	writeFile.close()
# 	print("Done!")


for url in link:
	data = scrapeSite(url)
	#writeToFile(data)