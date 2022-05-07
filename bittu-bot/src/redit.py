import os
import json
import cv2
import random
import requests
import time
import discord
import asyncpraw
from discord.utils import get
from discord.ext import commands, tasks

class Redit(commands.Cog):

	def __init__(self, client):
		self.client = client

		credentials = {
			"client_id": "client_id",
			"client_secret": "client_secret",
			"username": "username",
			"password": "password"
		}

		client_id = credentials['client_id']
		client_secret = credentials['client_secret']
		username = credentials['username']
		password = credentials['password']

		reddit = asyncpraw.Reddit(client_id = client_id, 
			client_secret = client_secret,
			user_agent = "For INDIA",
			username = username,
			password = password)

		self.reddit = reddit

		self.subreddits = ['DesiMemeCentral', 'test_our_bot']

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

	@commands.Cog.listener()
	async def on_message(self, message):

		reddit = self.reddit

		sendImage = False
		sendVideo = False
		flairs = []

		me = self.client.user

		if message.author == me:
			return
		if message.channel.id != 961861470558232646:
			return
		if message.content.startswith('.'):
			return

		title = f'Posted by {message.author}'
		sub = 'DesiMemeCentral'

		subreddit = await reddit.subreddit("DesiMemeCentral")
		async for flair in subreddit.flair.link_templates.user_selectable():
			temp1 = flair["flair_template_id"]
			temp2 = flair["flair_text"]
			flairs.append([temp1, temp2])

		FLAIR = random.choice(flairs)

		flair_id = FLAIR[0]
		flair_text = FLAIR[1]

		attachments = message.attachments

		if len(attachments) == 0:
			return

		if len(attachments) > 1:
			await message.channel.send('Too many arguments. leaving.', delete_after = 20)

		if len(attachments) == 1:
			attachment = attachments[0]

			if attachment.filename.endswith(".jpg") \
			or attachment.filename.endswith(".jpeg") \
			or attachment.filename.endswith(".png") \
			or attachment.filename.endswith(".webp"):
				sendImage = True
				url = attachment.url

				with open('image.jpg', 'wb') as handle:
					response = requests.get(url, stream=True)

					if not response.ok:
						print(response)

					for block in response.iter_content(1024):
						if not block:
							break

						handle.write(block)

			if attachment.filename.endswith(".mp4"):
				sendVideo = True
				url = attachment.url
				response = requests.request('GET', url = url)

				with open('video.mp4', 'wb') as file:
					file.write(response.content)

				vidcap = cv2.VideoCapture('video.mp4')
				success, image = vidcap.read()
				if success:
					cv2.imwrite("thumbnail.jpg", image)

			if sendImage:
				subreddit = await reddit.subreddit(sub)
				await subreddit.submit_image(title, image_path = './image.jpg', 
				send_replies = False, flair_id = flair_id, flair_text = flair_text)

			if sendVideo:
				subreddit = await reddit.subreddit(sub)
				await subreddit.submit_video(title, video_path = './video.mp4', 
				thumbnail_path = './thumbnail.jpg', send_replies = False, 
				flair_id = flair_id, flair_text = flair_text)

	@commands.command(aliases = ['sf', 'showFlair'])
	async def showFlairs(self, ctx, sub):
		reddit = self.reddit
		flairs = []

		try:
			subreddit = await reddit.subreddit(sub)
			async for flair in subreddit.flair.link_templates.user_selectable():
				temp1 = flair["flair_template_id"]
				temp2 = flair["flair_text"]
				flairs.append([temp1, temp2])

		except:
			await ctx.send(f'r/{sub} does not exist.')
			return

		if len(flairs) == 0:
			await ctx.send(f'{sub} does not have flairs. you do not need to use one while uploading.')
			return

		embed = discord.Embed(title = f'Flairs in r/{sub}', 
		color = discord.Color.from_rgb(125, 123, 234))

		for i in range(len(flairs)):
			embed.add_field(name = i, value = flairs[i][1])

		embed.set_footer(text = 'Use the given numbers in place of flairs while uploading via command.')

		await ctx.send(embed = embed)

	@commands.command(aliases = ['up'])
	async def upload(self, ctx, title, sub, flairIndex = None):
		reddit = self.reddit
		sendImage = False
		sendVideo = False
		flairs = []

		try:
			subreddit = await reddit.subreddit(sub)
			async for flair in subreddit.flair.link_templates.user_selectable():
				temp1 = flair["flair_template_id"]
				temp2 = flair["flair_text"]
				flairs.append([temp1, temp2])

		except:
			await ctx.send(f'r/{sub} does not exist.')
			return

		if flairIndex == None:
			flair_id = None
			flair_text = None

		if (flairIndex != None):
			flairIndex = int(flairIndex)
			if (flairIndex <= len(flairs)):
				flair_id = flairs[flairIndex][0]
				flair_text = flairs[flairIndex][1]

			else: 
				await ctx.send('No flair on that index. Leaving.')

		attachments = ctx.message.attachments

		if len(attachments) > 1:
			await ctx.send('Too many arguments. leaving.')
			return

		if len(attachments) == 0:
			await ctx.send('No images provided. leaving')
			return

		if len(attachments) == 1:
			attachment = attachments[0]

			if attachment.filename.endswith(".jpg") \
			or attachment.filename.endswith(".jpeg") \
			or attachment.filename.endswith(".png") \
			or attachment.filename.endswith(".webp"):
				sendImage = True
				url = attachment.url

				with open('image.jpg', 'wb') as handle:
					response = requests.get(url, stream=True)

					if not response.ok:
						print(response)

					for block in response.iter_content(1024):
						if not block:
							break

						handle.write(block)

			if attachment.filename.endswith(".mp4"):
				sendVideo = True
				url = attachment.url
				response = requests.request('GET', url = url)

				with open('video.mp4', 'wb') as file:
					file.write(response.content)

				vidcap = cv2.VideoCapture('video.mp4')
				success, image = vidcap.read()
				if success:
					cv2.imwrite("thumbnail.jpg", image)

			if sendImage:
				subreddit = await reddit.subreddit(sub)
				await subreddit.submit_image(title, image_path = './image.jpg', 
				send_replies = False, flair_id = flair_id, flair_text = flair_text)

			if sendVideo:
				subreddit = await reddit.subreddit(sub)
				await subreddit.submit_video(title, video_path = './video.mp4', 
					thumbnail_path = './thumbnail.jpg', send_replies = False, 
					flair_id = flair_id, flair_text = flair_text)

	@commands.command()
	@verify.is_mod()
	async def redinfo(self, ctx, username, limit = 100):
		if limit <= 9 or limit >= 1001:
			await ctx.send('too big comment history. terminating.')
			return 

		reddit = self.reddit
		user = await reddit.redditor(username)
		await user.load()

		avatar = user.icon_img
		karma = user.comment_karma
		link_karma = user.link_karma
		has_verified_email =  user.has_verified_email
		created_at = time.ctime(int(user.created_utc))

		liberandu = 0
		india = 0
		indiaspeaks = 0
		exhindu = 0
		otherlist = []
		frequencies = []
		msg = ''

		async for comment in user.comments.new(limit = limit):
			sub = str(comment.subreddit)
			sub = sub.lower()
			if sub == 'librandu':
				liberandu += 1
			elif sub == 'india':
				india += 1
			elif sub == 'indiaspeaks':
				indiaspeaks += 1
			elif sub == 'exhindu':
				exhindu += 1
			else:
				otherlist.append(sub)

		mylist = sorted(set(otherlist))

		for item in mylist:
			x = otherlist.count(item)
			frequencies.append([item, x])

		others = limit - liberandu - india - indiaspeaks

		for item in frequencies:
			msg = msg + f'{item[0]}: {item[1]}\n'

		embed = discord.Embed(description = msg, color = discord.Color.from_rgb(255,199,44))

		embed.add_field(name = 'Created at', value = created_at, inline = True)
		embed.add_field(name = 'Comment karma', value = karma, inline = True)
		embed.add_field(name = 'Link karma', value = link_karma, inline = True)
		embed.add_field(name = 'Verified email', value = has_verified_email, inline = True)
		embed.add_field(name = 'Liberandu', value = f'{liberandu} / {limit}', inline = True)
		embed.add_field(name = 'India', value = f'{india} / {limit}', inline = True)
		embed.add_field(name = 'Indiaspeaks', value = f'{indiaspeaks} / {limit}', inline = True)
		embed.add_field(name = 'Exhindu', value = f'{exhindu} / {limit}', inline = True)
		embed.add_field(name = 'others', value = f'{others} / {limit}', inline = True)
		
		embed.set_author(name = f'u/{user.name}', icon_url = avatar)
		await ctx.send(embed = embed)

def setup(client):
	client.add_cog(Redit(client))


