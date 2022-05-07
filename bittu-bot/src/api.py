import discord
from discord.ext import commands
import requests
import json

class Apis(commands.Cog):

	def __init__(self, client):
		self.client = client

def setup(client):
	client.add_cog(Apis(client))