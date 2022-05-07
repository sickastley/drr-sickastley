import discord
from discord.ext import commands
import json
import random
import string
import csv

class Hindi(commands.Cog):

	def __init__(self, client):
		self.client = client

	async def get_wordList(self):
		wordList = []

		with open("__hindi.csv", "r") as file:
			data = csv.reader(file)
			
			for row in data:
				row[0], row[1] = row[0].lower(), row[1].lower()
				wordList.append(row)

			wordList = wordList[1: ]

		return wordList

	async def getReply(self, word, wordList):
		temp = []
		for item in wordList:
			if item[0] == word:
				temp.append(item[1].capitalize())

		alternative = ", ".join(temp)

		STR = f"{word.capitalize()} ❌ {alternative} :white_check_mark:"

		return STR

	async def checkForAlt(self, word, lst, wordList):
		temp = []
		for item in wordList:
			if item[0] == word:
				temp.append(item[1])

		return any(alt in lst for alt in temp)

	@commands.Cog.listener()
	async def on_message(self, message):

		if message.content.startswith('$') \
		or message.content.startswith('.') \
		or message.author == self.client.user:
			pass

		else:

			content = message.content.lower()
			content = content.translate(str.maketrans('', '', string.punctuation))
			lst = content.split(" ")

			wordList = await self.get_wordList()

			found = []
			replylst = []

			for item in wordList:
				for word in lst:
					if item[0] == word:
						if word not in found:
							found.append(word)

			if len(found) > 0:
				for word in found:
					if await self.checkForAlt(word, lst, wordList):
						found.remove(word)
					else:
						pass

				text = ''

				for word in found:
					__reply__ = await self.getReply(word, wordList)
					text = text + __reply__ + '\n'
				await message.reply(text, delete_after = 30)

def setup(client):
	client.add_cog(Hindi(client))
