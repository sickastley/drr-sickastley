import praw
import sys
import csv
import json
import time
from datetime import datetime

with open("config.json", "r") as file:

	data = json.load(file)

	client_id = data["client_id"]
	client_secret = data["client_secret"]
	username = data["username"]
	password = data["password"]

reddit = praw.Reddit(client_id = client_id, 
	client_secret = client_secret,
	user_agent = "for INDIA",
	username = username,
	password = password)

users = []
sent = []
temp =[]
toSend = []

with open("users.csv", "r") as file:
	csv1 = csv.reader(file)
	for row in csv1:
		users.append(row[0])

with open("sent.csv", "r") as file:
	csv1 = csv.reader(file)
	for row in csv1:
		sent.append(row[0])

for item in users:
	if item not in sent:
		toSend.append(item)

def ratelim(string):

	lst = string.split(" ")
	kek = int(lst[13])

	return kek

def add(user):
	with open("sent.csv", "a", newline = '') as file:
		writer = csv.writer(file)

		writer.writerow([user])

title = "Hello There!"
string = '''
I am very inspired by your profile here. You seem to be a great person. I like the way you roll.
are you acitve in bakchodi[dot]org website?? I would like to follow you up there as I am switching to Indian from foreign platforms.
if you haven't already joined, you can join it!

Thanks for reading :)'''

for user in toSend:

	try:
		reddit.redditor(user).message(title, string)
		t = str(datetime.now())
		t = t[:-6]
		print(f"{t} User: {user}, Status: Success")

		add(user)

	except praw.exceptions.RedditAPIException as exception:

		for subexception in exception.items:
			t = str(datetime.now())
			t = t[:-6]

			if subexception.error_type == "NOT_WHITELISTED_BY_USER_MESSAGE":
				add(user)
				print(f"{t} User: {user}, Status: Failed, Reason: Not Whitelisted.")

			elif subexception.error_type == "RATELIMIT":
				kek = ratelim(str(subexception))
				kekinsecs = (kek * 60) + 15
				print(f"{t} Ratelimited for {kek} minutes, sleeping for {kekinsecs} seconds...")
				time.sleep(kekinsecs)

			elif subexception.error_type == "USER_DOESNT_EXIST":
				add(user)
				print(f"{t} User: {user}, Status: Failed, Reason: User Dead.")

			elif subexception.error_type == "INVALID_USER":
				add(user)
				print(f"{t} User: {user}, Status: Failed, Reason: User Invalid.")

			else:
				print(subexception.error_type)

	time.sleep(29)



