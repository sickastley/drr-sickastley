import os
import discord
import random
import json
import discord
from discord.utils import get
from discord.ext import commands

class Mods(commands.Cog):
	
	def __init__(self, client):
		self.client = client

	def loadJson(self, file):
		with open(file, 'r') as f:
			return json.load(f)

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

	@commands.command()
	@verify.is_mod()
	async def clear(self, ctx, limit = 1):
		await ctx.channel.purge(limit = limit + 1)

	@commands.command()
	@verify.is_mod()
	async def giverole(self, ctx, member: discord.Member, role: discord.Role):
		await member.add_roles(role)
		await ctx.send(f"given @{role} to {member}.")

	@commands.command()
	@verify.is_mod()
	async def takerole(self, ctx, member: discord.Member, role: discord.Role):
		await member.remove_roles(role)
		await ctx.send(f"taken @{role} from {member}.")

	@commands.command()
	@verify.is_mod()
	async def echo(self, ctx, channel: discord.TextChannel, *, message):
		await channel.send(message)

	@commands.command()
	@verify.is_mod()
	async def dm(self, ctx, member: discord.Member, *, message):
		await member.send(message)

	@commands.command()
	@verify.is_mod()
	async def kick(self, ctx, member: discord.Member, *, reason = None):
		await member.send(f'Kicked. Reason: {reason}')
		await member.kick()
		await ctx.send(f'Kicked {member}. reason: {reason}')

	@commands.command()
	@verify.is_mod()
	async def ban(self, ctx, member: discord.Member, *, reason = None):
		await member.send(f'Banned. Reason: {reason}')
		await member.ban()
		await ctx.send(f'Banned {member}. reason: {reason}')

	@commands.command()
	@verify.is_mod()
	async def unban(self, ctx, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split("#")

		for ban_entry in banned_users:
			user = ban_entry.user
			
			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'Unbanned {member}')

				return
	
	@commands.command()
	@verify.is_mod()
	async def userinfo(self, ctx, member: discord.Member):
		joined_at = member.joined_at.strftime('%b %d, %Y, %T')
		created_at = member.created_at.strftime('%b %d, %Y, %T')
		avatar = member.avatar_url

		embed = discord.Embed(color = discord.Color.from_rgb(114,137,218))

		embed.add_field(name = 'Joined at', value = joined_at, inline = True)
		embed.add_field(name = 'Created at', value = created_at, inline = True)

		embed.set_author(name = member, icon_url = avatar)

		await ctx.send(embed = embed)

	@commands.command()
	@verify.is_mod()
	async def avatar(self, ctx, member: discord.Member):
		if member == None:
			await ctx.send(ctx.author.avatar_url)
		else:
			await ctx.send(member.avatar_url)

def setup(client):
	client.add_cog(Mods(client))