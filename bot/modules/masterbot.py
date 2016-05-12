#!/usr/bin/env python3
# -*-coding:Latin-1 -*
import discord
import logging
import asyncio
from .backtask import BackgroundTasks

class Masterbot(discord.Client):

	def __init__(self, *args, **kwargs):
		print("Initialisation du bot {0}".format(id(self)))
		super(Masterbot, self).__init__(*args, **kwargs)
		self.prefix = kwargs.get('command_prefix')
		self.description = kwargs.get('description')

	async def on_ready(self):
		print("bot :"+format(id(self))+" ready !")

	async def on_message(self, message):
	        #check spam here
	        if message.channel.is_private:
	            return

	        server = message.server
	        print(message.content)
	        if message.content == self.prefix+"ping":
	        	await self.send_message(message.channel, "Pong !")

	async def roll(self, dice : str):
	    """Rolls a dice in NdN format."""
	    try:
	        rolls, limit = map(int, dice.split('d'))
	    except Exception:
	        await self.say('Format has to be in NdN!')
	        return

	    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	    await self.say(result)