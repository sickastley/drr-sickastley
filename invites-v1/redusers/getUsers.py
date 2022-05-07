import praw
import sys
import csv
import json
import time
import argparse

parser = argparse.ArgumentParser(description = "Dharmo Rakshati Rakshitah")

parser.add_argument("-s", "--subreddit", 
	dest = "subreddit", 
	default = "indiaspeaks", 
	help = "the subbreddit to scan, without u/.")

parser.add_argument("-t", "--scanType", 
	dest ="scanType", 
	default = "main",
	help = "scantype, main/bulk. main searches active comments.\nbulk searches for old comments.")

parser.add_argument("-l", "--limit", 
	dest = "limit", 
	type=int, 
	default = None,
	help = "numbers of comments to be searched.\nno need to use with main.")

parser.add_argument("-f", "--saveFile", 
	dest = "saveFile", 
	type=str, 
	default = "users.csv",
	help = "saveFile name. default = users.csv.\nif file is already present, appends to the previous one.")

args = parser.parse_args()

subreddit = args.subreddit
scanType = args.scanType
limit = args.limit
saveFile = args.saveFile

try:
	with open(saveFile, "r") as file:
		pass

except:
	with open(saveFile, "w") as file:
		pass

with open("config.json", "r") as file:

	data = json.load(file)

	client_id = data["client_id"]
	client_secret = data["client_secret"]
	username = data["username"]
	password = data["password"]

reddit = praw.Reddit(client_id = client_id, 
	client_secret = client_secret,
	user_agent = "For INDIA",
	username = username,
	password = password)

ME = reddit.user.me()

prohibited = [ME, "AutoModerator", "None", "savevideobot", "SaveVideo"]

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


def main():

	comments = reddit.subreddit(subreddit).stream.comments(skip_existing=True)

	for comment in comments:
		user = str(comment.author)
		if user not in prohibited:
			checkcsv(user, saveFile)

		else:
			pass

def bulk():

	comments = reddit.subreddit(subreddit).comments(limit=limit)

	for comment in comments:
		user = str(comment.author)
		if user not in prohibited:
			checkcsv(user, saveFile)

		else:
			pass


print(f'''
Starting scan...
Subreddit: {subreddit}
Scan Type: {scanType}
Savefile: {saveFile}
''')


if scanType == "main":
	while True:
		main()

if scanType == "bulk":
	while True:
		bulk()
		
else:
	while True:
		main()


