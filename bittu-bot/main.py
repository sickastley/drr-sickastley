import os
import json
import discord
import requests
import json
from discord.utils import get
from discord.ext import commands

class verify():
	def is_me():
		return commands.is_owner()

	def is_mod():
		return commands.has_permissions(
			manage_messages = True,
			kick_members = True,
			ban_members = True)

	def is_admin():
		return commands.has_permissions(
			administrator = True)

command_prefix = [
	'$', 
	'pitaji ',
	'bittu ',
	'modiji ']

activity = discord.Activity(type = discord.ActivityType.watching)
status = discord.Status.idle

intents = discord.Intents.all()
client = commands.Bot(
	command_prefix = command_prefix,
	activity = activity,
	status = status,
	intents = intents)

@client.event
async def on_ready():
	print(f'Logged in as {client.user}')
	await client.change_presence(
		activity = discord.Activity(
			type = discord.ActivityType.watching, 
			name = f'{len(client.users)} Sanatanis'), 
			status = discord.Status.idle)

@client.command()
@verify.is_me()
async def load(ctx, extension):
	client.load_extension(f"src.{extension}")
	await ctx.send("Load successfull.")

@client.command()
@verify.is_me()
async def unload(ctx, extension):
	client.unload_extension(f"src.{extension}")
	await ctx.send("Unload successfull.")

@client.command()
@verify.is_me()
async def reload(ctx, extension):
	client.unload_extension(f"src.{extension}")
	client.load_extension(f"src.{extension}")
	await ctx.send("Reload successfull.")

@client.command()
async def load_all(ctx):
	for filename in os.listdir("./src"):
		if filename.endswith(".py"):
			filename = filename[:-3]
			client.load_extension(f"src.{filename}")
	await ctx.send("All extensions loaded successfully.")

@client.command()
@verify.is_me()
async def unload_all(ctx):
	for filename in os.listdir("./src"):
		if filename.endswith(".py"):
			filename = filename[:-3]
			client.unload_extension(f"src.{filename}")
	await ctx.send("All extensions unloaded successfully.")

@client.command()
@verify.is_me()
async def reload_all(ctx):
	for filename in os.listdir("./src"):
		if filename.endswith(".py"):
			filename = filename[:-3]
			client.unload_extension(f"src.{filename}")
			client.load_extension(f"src.{filename}")
	await ctx.send("All extensions reloaded successfully.")

for filename in os.listdir("./src"):
	if filename.endswith(".py"):
		filename = filename[:-3]
		client.load_extension(f"src.{filename}")

TOKEN = ''
client.run(TOKEN)