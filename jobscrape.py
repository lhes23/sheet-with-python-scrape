import requests
from bs4 import BeautifulSoup
import csv
import os

# links to be scrape
link = [
	"https://www.onlinejobs.ph/jobseekers/jobsearch",
	"https://www.onlinejobs.ph/jobseekers/jobsearch/30",
	"https://www.onlinejobs.ph/jobseekers/jobsearch/60",
]

#Initiate the list
data = []


# function for scraping the site
def scrapeSite(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text,'html.parser')
	section = soup.find('section',{'class':'bg-lwhite'})
	div = section.find('div',{'class':'col-md-7'})
	div.find('div',{'class':'text-center'}).decompose()

	a = div.find_all('a')
	for job in a:
		for jobs_box in job.find_all('div',{'class':'jobs-box'}):
			title = jobs_box.find_all('p')[0].text.strip()
			category = jobs_box.find_all('p')[1].text.strip()
			salary = jobs_box.find_all('p')[2].text.strip()
			details = jobs_box.find_all('p')[4].text.strip()
		link = job.get('href')
		data.append([title, category, salary, details, link])
	return data

# write to CSV file
def writeToFile(data):
	with open('jobs.csv','w') as writeFile:
		writer = csv.writer(writeFile)
		writer.writerows(data)
	writeFile.close()
	

# Process the links
for url in link:
	data = scrapeSite(url)
	writeToFile(data)
print('Done!')