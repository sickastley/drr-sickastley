import discord
import random
from discord.utils import get
from discord.ext import commands, tasks

class Beta(commands.Cog):
	def __init__(self, client):
		self.client = client

	TESTER = 'beta-tester'

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

	# @tasks.loop(seconds = 10)
	# async def myLoop(self):
	#     channel = self.client.get_channel(967813899435008000)
	#     await channel.send("Test Message")

	# @commands.command()
	# async def start(self, ctx):
	# 	self.myLoop.start()

	# @commands.command()
	# async def stop(self, ctx):
	# 	self.myLoop.stop()

	@commands.command(aliases = ['rp'])
	@commands.has_role(TESTER)
	@verify.is_mod()
	async def refreshPresence(self, ctx):
		await self.client.change_presence(
			activity = discord.Activity(
				type = discord.ActivityType.watching, 
				name = f'{len(self.client.users)} Sanatanis'), 
				status = discord.Status.idle)

	@commands.command(aliases = ['imp'])
	@commands.has_role(TESTER)
	@verify.is_mod()
	async def impersonate(
		self, ctx,
		 user: discord.Member,
		  channel: discord.TextChannel, *,
		   message: str):

		webhooks = await channel.webhooks()

		if len(webhooks) == 0:
			await channel.create_webhook(name = 'created by bittu')

		webhooks = await channel.webhooks()
		for webhook in webhooks:
			await webhook.send(
				message, 
				username = user.name, 
				avatar_url = user.avatar_url)

			return

	@commands.command(aliases = ['imp2'])
	@verify.is_me()
	async def impersonateAdv(
		self, 
		ctx, 
		user: discord.Member, 
		channel: discord.TextChannel,
		username,
		*, 
		message: str):
		webhooks = await channel.webhooks()

		if len(webhooks) == 0:
			await channel.create_webhook(name = 'created by bittu')

		webhooks = await channel.webhooks()
		for webhook in webhooks:
			await webhook.send(
				message, 
				username = username, 
				avatar_url = user.avatar_url)

			return

def setup(client):
	client.add_cog(Beta(client))


