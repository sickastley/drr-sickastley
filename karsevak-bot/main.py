import praw
import csv
import time
import json
import sys
import string
from datetime import datetime

wordList = []
blacklist = []

devs = sys.argv[1]

#############################################################
with open("Hindi.csv", "r") as file:
	data = csv.reader(file)
	
	for row in data:
		row[0], row[1] = row[0].lower(), row[1].lower()
		wordList.append(row)

	wordList = wordList[1: ]
#############################################################
with open("config.json", "r") as file:
	data = json.load(file)

	client_id = data["client_id"]
	client_secret = data["client_secret"]
	username = data["username"]
	password = data["password"]
#############################################################
with open("blacklisted.csv", "r") as file:
	data = csv.reader(file)
	
	for row in data:
		blacklist.append(row[0])
#############################################################
reddit = praw.Reddit(client_id = client_id, 
	client_secret = client_secret,
	user_agent = "testing by u/not-karsevak",
	username = username,
	password = password)

ME = reddit.user.me()
#SUBREDDIT = "test_our_bot"
SUBREDDIT = "Chodi"
#############################################################
def getReply(word):
	temp = []
	for item in wordList:
		if item[0] == word:
			temp.append(item[1].capitalize())

	alternative = ", ".join(temp)

	STR = f"{word.capitalize()} ❌ {alternative} ✔️"

	return STR
#############################################################
def checkForAlt(word, lst):
	temp = []
	for item in wordList:
		if item[0] == word:
			temp.append(item[1])

	if any(alt in lst for alt in temp):
		return True

	else: 
		return False
#############################################################
def main():

	for comment in reddit.subreddit(SUBREDDIT).stream.comments(skip_existing=True):

		if comment.author in blacklist:
			continue

		if hasattr(comment, "body") and comment.author != ME:
			comment_lower = comment.body.lower()
			comment_lower = comment_lower.translate(str.maketrans('', '', string.punctuation))
			lst = comment_lower.split(" ")

			found = []

			for item in wordList:
				for word in lst:
					if item[0] == word:
						if word not in found:
							found.append(word)

			if len(found) > 0:
				for word in found:
					if checkForAlt(word, lst):
						found.remove(word)
					else:
						pass

				for word in found:
					__reply__ = getReply(word)
					comment.reply(__reply__)
					print(__reply__)
					time.sleep(4)

			else:
				pass
#############################################################
def monitor():

	found = []

	for comment in reddit.subreddit(SUBREDDIT).stream.comments(skip_existing=True):

		if comment.author in blacklist:
			continue

		if hasattr(comment, "body") and comment.author != ME:
			comment_lower = comment.body.lower()
			comment_lower = comment_lower.translate(str.maketrans('', '', string.punctuation))
			lst = comment_lower.split(" ")

			for item in wordList:
				for word in lst:
					if item[0] == word:
						if word not in found:
							found.append(word)

			print(found)
			found = []
			print(comment_lower)
#############################################################				

if devs == "main":
	while True:
		print("Running Main...")
		main()

if devs == "monitor":
	while True:
		print("Running Monitor...")
		monitor()