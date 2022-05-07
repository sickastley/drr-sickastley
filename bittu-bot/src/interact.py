import discord
from discord.ext import commands
import requests
import json
import random

class Interactive(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, message):

		if not message.content.startswith('>'):
			return

		authheaderKEYpair = [
		["authorization", "xrapidapikey"], 
		["authorization", "xrapidapikey"]] 

		"""api version of this: https://pypi.org/project/prsaw2/"""

		this = random.choice(authheaderKEYpair)

		authorization = this[0]
		xrapidapikey = this[1]

		url = "https://random-stuff-api.p.rapidapi.com/ai"

		querystring = {"msg":f"{message.content}", 
		"bot_name":"Pitaji",
		"bot_gender":"male",
		"bot_master":"Aman",
		"bot_age":"19",
		"bot_company":"Neptunes aerospace",
		"bot_location":"India",
		"bot_email":"chaos69480@gmail.com",
		"bot_build":"Not really public",
		"bot_birth_year":"2002",
		"bot_birth_date":"12 January, 2002",
		"bot_birth_place":"India",
		"bot_favorite_color":"Orange",
		"bot_favorite_book":"Hari puttar",
		"bot_favorite_band":"AC DC",
		"bot_favorite_artist":"Skrillex",
		"bot_favorite_actress":"Ananya pandey",
		"bot_favorite_actor":"Karan johar",
		"id":message.author.id}

		headers = {
			'authorization': f"{authorization}",
			'x-rapidapi-host': "random-stuff-api.p.rapidapi.com",
			'x-rapidapi-key': f"{xrapidapikey}"
			}

		me = self.client.user.id

		if message.content.startswith("!"):
			return
		if message.author.id == me:
			return

		response = requests.request("GET", url, headers=headers, params=querystring)
		data = json.loads(response.text)
		
		reply = data["AIResponse"]
		await message.reply(reply)

def setup(client):
	client.add_cog(Interactive(client))
