import discord
from discord.ext import commands

class Errors(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		await ctx.send(error, delete_after = 7)
			
def setup(client):
		client.add_cog(Errors(client))