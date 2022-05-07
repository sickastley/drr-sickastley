import requests
import csv
import time
from bs4 import BeautifulSoup

url = "https://pholder.com/r/chodi/?page="
pages = 65
raw = []

def adduser(user, File):
	with open(File, "a", newline = '') as file:
		writer = csv.writer(file)
		temp = []
		temp.insert(0, [user])
		for item in temp:
			writer.writerow(item)

def checkcsv(user, File):
	userlist = []
	temp = []
	with open(File, "r") as file:
		csv1 = csv.reader(file)
		for row in csv1:
			temp.append(row)

		for item in temp:
			userlist.append(item[0])

	if user in userlist:
		print(f"In Database: {user}")
		return
	if user not in userlist:
		adduser(user, File)
		print(f"Added user: {user}")

def main(url, pages):
	for i in range(1, pages + 1):
		URL = url + str(i)

		response = requests.request("GET", URL)
		soup = BeautifulSoup(response.text, 'lxml')

		for link in soup.find_all('a'):
			kek = link.get('href')

			raw.append(kek)

	print("Fetched raw data. starting search in 3 secs...")
	time.sleep(3)

	for item in raw:
		if item[:3] == "/u/":

			username = item[3: -1]

			checkcsv(username, "chodi.csv")

main(url, pages)

