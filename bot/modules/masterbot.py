#!/usr/bin/env python3
# -*-coding:Latin-1 -*
import discord
import logging
import asyncio
import json

class Masterbot(discord.Client):

	mygame = 'useless forever'

	def __init__(self, *args, **kwargs):
		super(Masterbot, self).__init__(*args, **kwargs)
		self.prefix = kwargs.get('command_prefix')
		self.description = kwargs.get('description')
		print("Initialisation of bot {0}".format(id(self))+" completed.")
		print("ARGS: "+str(args))
		print("###################################")
		print("KWARGS: "+str(kwargs))

	async def on_ready(self):
		print('------')
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')
		await self.change_status(
				game=discord.Game(
			    name=self.mygame
			)
		)

	async def send_message(self, *args, **kwargs):
		return await super().send_message(*args, **kwargs)

	async def on_message(self, message):

		if message.channel.is_private:
			return

		if message.content == self.prefix+'clear':
			deleted_messages = await self.purge_from(
				message.channel,
				limit=1001
			)

			message_number = len(deleted_messages) - 1

			confirm_message = await self.send_message(
				message.channel,
					"`Deleted {} message{}!` :thumbsup: ".format(
					message_number,
					"" if message_number < 2 else "s"
				)
			)
			await asyncio.sleep(3)

			await self.delete_message(confirm_message)

		if message.content == self.prefix+"ping":
			await self.send_message(message.channel, "Pong !")

		if message.content == self.prefix+"test":
			await self.send_message(message.channel, message.channel)

		print(message.content)

		if message.content == self.prefix+"ping":
			await self.send_message(message.channel, "Pong !")