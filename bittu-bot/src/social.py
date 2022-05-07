import os
import discord
import random
import json
import asyncio
from discord.ext import commands
import requests


class Social(commands.Cog):

	def __init__(self, client):
		self.client = client

	async def loadJson(self, file):
		with open(file, 'r') as f:
			return json.load(f)

	@commands.command()
	async def ping(self, ctx):
		await ctx.send(f'client latency: {round(self.client.latency * 1000)} ms')

	@commands.command()
	async def calc(self, ctx, *, kek):
		try:
			await ctx.send(eval(kek))
		except: await ctx.send('ask your mom')

	@commands.command()
	async def nick(self, ctx, choice = 0):
		user: discord.Member = ctx.author

		data = await self.loadJson('__config.json')

		names = data["names"]
		titles = data["titles"]

		name = random.choice(names)
		title = random.choice(titles)

		if choice == 0:
			final = name + ' ' + title

		if choice == 1:
			final = name

		if choice == 2:
			final = title

		await user.edit(nick = name)

	@commands.command()
	async def rid(self, ctx):

		url = f"https://randomuser.me/api/"

		response = requests.request("GET", url)
		json_data = json.loads(response.text)
		
		gender = json_data["results"][0]["gender"]
		title = json_data["results"][0]["name"]["title"]
		first = json_data["results"][0]["name"]["first"]
		last = json_data["results"][0]["name"]["last"]
		number = json_data["results"][0]["location"]["street"]["number"]
		name = json_data["results"][0]["location"]["street"]["name"]
		city = json_data["results"][0]["location"]["city"]
		state = json_data["results"][0]["location"]["state"]
		country = json_data["results"][0]["location"]["country"]
		postcode = json_data["results"][0]["location"]["postcode"]
		email = json_data["results"][0]["email"]
		dob = json_data["results"][0]["dob"]["date"]
		age = json_data["results"][0]["dob"]["age"]
		picture = json_data["results"][0]["picture"]["large"]
		
		domain = ["gmail.com", "yahoo.com", "linuxdevs", "parle.biz", "britannia.com", "itsols.com", "xiaomi.com"]
		email = email[:-11]
		email = email + random.choice(domain)
		
		dob = dob[:-14]
		
		embed = discord.Embed(title = f"Fake ID",
							  description = f"Name: {title} {first} {last}\nDOB: {dob}\nAge: {age}\nGender: {gender}\nAddress: {number}, {name}, {city},\n{state}, {country}, Postcode: {postcode}.\nEmail: {email}",
							  color = discord.Color.from_rgb(random.randint(0, 266), random.randint(0, 266), random.randint(0, 266)))
		embed.set_image(url = f"{picture}")
		embed.set_footer(text = f"Note: This is a Random and Fake User ID,\ngenerated for fun purposes only.")
		
		await ctx.send(embed = embed)

	@commands.command(aliases = ["def", "?"])
	async def define(self, ctx, *, word):
		url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

		response = requests.request("GET", url)

		data = json.loads(response.text)

		try:
			title = data["title"]
			message = data["message"]

			embed = discord.Embed(title = title, 
				description = message, 
				color = discord.Colour.from_rgb(255, 0, 0))

			await ctx.send(embed = embed, delete_after = 5)

		except:
			word = data[0]["word"]

			meaning = data[0]["meanings"][0]["definitions"][0]["definition"]

			embed = discord.Embed(title = word, 
				description = meaning, 
				color = discord.Colour.from_rgb(255, 229, 180))

			embed.set_author(name = "Dictionary")
			embed.set_footer(text = "Source: Wikipidea")
			await ctx.send(embed = embed)

	@commands.command()
	async def fact(self, ctx):
		url = "https://uselessfacts.jsph.pl/random.json?language=en"

		response = requests.request("GET", url)
		data = json.loads(response.text)
		fact = data["text"]

		embed = discord.Embed(title = f"Useless fact",
			description = f"{fact}",
			color = discord.Color.from_rgb(202, 239, 209))

		await ctx.send(embed = embed)

	@commands.command(aliases = ["SunTzu", "Technoblade"])
	async def inspire(self, ctx):
		url = "https://zenquotes.io/api/random"

		response = requests.request("GET", url)
		data = json.loads(response.text)
		quote = data[0]['q']
		
		embed = discord.Embed(title = f"Inspiring Quote",
			description = quote,
			color = discord.Color.from_rgb(253, 253, 150))

		embed.set_footer(text = "-Sun Tzu, The art of War.")

		await ctx.send(embed = embed)

	@commands.command(aliases = ["norris"])
	async def chuck(self, ctx):
		url = "https://api.chucknorris.io/jokes/random"

		response = requests.request("GET", url)
		data = json.loads(response.text)
		fact = data["value"]
		
		embed = discord.Embed(title = "Fact",
			description = fact,
			color = discord.Color.from_rgb(253, 128, 128))

		await ctx.send(embed = embed)

	@commands.command(aliases = ["suggest"])
	async def advice(self, ctx):
		url = "https://api.adviceslip.com/advice"

		response = requests.request("GET", url)
		data = json.loads(response.text)
		advice = data["slip"]["advice"]
		
		embed = discord.Embed(title = f"Advice",
			description = advice,
			color = discord.Color.from_rgb(128, 253, 128))

		await ctx.send(embed = embed)

	@commands.command()
	async def weather(self, ctx, *, place):

		url = f"http://api.weatherapi.com/v1/current.json"

		params = {
		"key": "get your api key sucker",
		"q": place
		}

		response = requests.request("GET", url, params = params)
		json_data = json.loads(response.text)
		
		name = json_data["location"]["name"]
		region = json_data["location"]["region"]
		country = json_data["location"]["country"]
		latitude = json_data["location"]["lat"] 
		longitude = json_data["location"]["lon"]
		local_date, local_time = json_data["location"]["localtime"].split(" ")
		last_updated_date, last_updated_time = json_data["current"]["last_updated"].split(" ")
		temp_c = json_data["current"]["temp_c"]
		temp_f = json_data["current"]["temp_f"]
		day_or_night = json_data["current"]["is_day"]
		text = json_data["current"]["condition"]["text"]
		icon = json_data["current"]["condition"]["icon"]
		wind_kph = json_data["current"]["wind_kph"]
		wind_mph = json_data["current"]["wind_mph"]
		wind_degree = json_data["current"]["wind_degree"]
		wind_dir = json_data["current"]["wind_dir"]
		pressure_mb = json_data["current"]["pressure_mb"]
		pressure_in = json_data["current"]["pressure_in"] 
		precip_mm = json_data["current"]["precip_mm"]
		precip_in = json_data["current"]["precip_in"]
		humidity = json_data["current"]["humidity"]
		cloud = json_data["current"]["cloud"]
		feelslike_c = json_data["current"]["feelslike_c"]
		feelslike_f = json_data["current"]["feelslike_f"]
		vis_km = json_data["current"]["vis_km"]
		vis_miles = json_data["current"]["vis_miles"]
		uv = json_data["current"]["uv"]
		gust_mph = json_data["current"]["gust_mph"]
		gust_kph = json_data["current"]["gust_kph"]
		
		if day_or_night == 1:
			exact = "Day"
		elif day_or_night == 0:
			exact = "Night"
		
		embed = discord.Embed(title = f"{name}'s Weather: {text}",
			color = discord.Color.from_rgb(128, 128, 253))

		embed.add_field(name = "Place", value = f"{name}, {region}, {country}", inline = True)
		embed.add_field(name = "Latitude", value = latitude, inline = True)
		embed.add_field(name = "Longitude", value = longitude, inline = True)
		embed.add_field(name = "Date", value = local_date, inline = True)
		embed.add_field(name = "Time", value = local_time, inline = True)
		embed.add_field(name = "Temperature", value = f"{temp_c} Celcius", inline = True)
		embed.add_field(name = "Feels like", value = f"{feelslike_c} Celcius", inline = True)
		embed.add_field(name = "Wind speed", value = wind_kph, inline = True)
		embed.add_field(name = "Wind degree", value = wind_degree, inline = True)
		embed.add_field(name = "Wind direction", value = wind_dir, inline = True)
		embed.add_field(name = "Humidity", value = humidity, inline = True)
		embed.add_field(name = "Clouds", value = cloud, inline = True)
		embed.add_field(name = "Visibility", value = vis_km, inline = True)
		embed.add_field(name = "Gust speed", value = gust_kph, inline = True)

		embed.set_footer(text = f"Last updated: {last_updated_date}, {last_updated_time}")
		
		await ctx.send(embed = embed)

	@commands.command()
	async def joke(self, ctx):
		url = "https://icanhazdadjoke.com/"
		
		headers = {
			"accept" : "application/json"
			}
		
		response = requests.request("GET", url, headers = headers)
		data = json.loads(response.text)
		joke = data["joke"]
		
		embed = discord.Embed(title = "Joke",
			description = joke, 
			color = discord.Color.from_rgb(100, 100, 253))
		
		await ctx.send(embed = embed)

	@commands.command()
	async def affirm(self, ctx):
		url = "https://www.affirmations.dev/"

		response = requests.request("GET", url)
		data = json.loads(response.text)
		affirmation = data["affirmation"]
		
		embed = discord.Embed(title = "Affirmation",
			description = affirmation,
			color = discord.Color.from_rgb(100, 253, 99))
		
		await ctx.send(embed = embed)

	@commands.command()
	async def codejoke(self, ctx):
		url = "https://geek-jokes.sameerkumar.website/api"

		params = {
			"format" : "json"
		}

		response = requests.request("GET", url, params = params)
		data = json.loads(response.text)
		joke = data["joke"]
		
		embed = discord.Embed(title = "Code Joke",
			description = joke,
			color = discord.Color.from_rgb(69, 138, 69))
		
		await ctx.send(embed = embed)

	@commands.command(aliases = ["apod"])
	@commands.cooldown(1, 10)
	async def a_picture_of_day(self, ctx):
		url = f'https://api.nasa.gov/planetary/apod'

		params = {
			"api_key" : "nasa api, free. keep in mind the devs there keep changing the format : ("
		}

		response = requests.request("GET", url, params = params)
		data = json.loads(response.text)

		copyright = data['copyright']
		date = data['date']
		explanation = data['explanation']
		hdurl = data['hdurl']
		title = data['title']

		embed = discord.Embed(title = title, 
			description = explanation, 
			color = discord.Color.from_rgb(198, 59, 127))

		embed.set_image(url = hdurl)
		embed.set_author(name = copyright)
		embed.set_footer(text = f"taken on {date}.")
		await ctx.send(embed = embed)

	@commands.command()
	@commands.cooldown(1, 10)
	async def meme(self, ctx):

		url = f'https://meme-api.herokuapp.com/gimme'
		response = requests.request("GET", url)
		data = json.loads(response.text)

		img_url = data["url"]
		img_author = data["author"]
		img_postLink = data["postLink"]

		embed = discord.Embed()
		embed.set_image(url=img_url)
		embed.set_author(name=img_author)

		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Social(client))
