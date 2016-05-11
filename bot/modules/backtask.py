#!/usr/bin/env python3
# -*-coding:Latin-1 -*
import discord
from time import time
import asyncio

class BackgroundTasks():

	def __init__(self):
		self.bot = bot

	async def my_background_task():
		await bot.wait_until_ready()
		counter = 0
		channel = discord.Object(id=botchan)
		while not bot.is_closed:
			#return True
		    counter += 1
		    await bot.send_message(channel, "test: "+counter)
		    await asyncio.sleep(60) # task runs every 60 seconds

		loop = asyncio.get_event_loop()

		try:
			loop.create_task(my_background_task())
			loop.run_until_complete(bot.login(token))
			loop.run_until_complete(bot.connect())
		except Exception:
			loop.run_until_complete(bot.close())
		finally:
			loop.close()