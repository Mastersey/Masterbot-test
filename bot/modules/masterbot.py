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
		print("bot :"+str(self)+" ready !")

	async def roll(dice : str):
	    """Rolls a dice in NdN format."""
	    try:
	        rolls, limit = map(int, dice.split('d'))
	    except Exception:
	        await self.say('Format has to be in NdN!')
	        return

	    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	    await self.say(result)

	#async def on_ready(self):
    	#pass