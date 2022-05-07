import discord
import string
import json
from discord.ext import commands

class Triggers(commands.Cog):

	def __init__(self, client):
		self.client = client

	def loadJson(self, file):
		with open(file, 'r') as f:
			return json.load(f)

	@commands.Cog.listener()
	async def on_message(self, message):

		content = message.content.lower()
		content = content.translate(str.maketrans('', '', string.punctuation))
		lst = content.split(" ")

		data = self.loadJson('__triggers.json')

		for key in data:
			if any(key == x for x in lst):
				await message.reply(data[key], delete_after = 10)

def setup(client):
	client.add_cog(Triggers(client))
