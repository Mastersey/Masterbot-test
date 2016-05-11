#!/usr/bin/env python3
# -*-coding:Latin-1 -*
import sys
import discord
from discord.ext import commands
import random
import re ## Imports Regex (Prefered for Commands)
import asyncio ## Part of Discord for asyncronous features
import os
import logging
from random import *
from math import *

botchan = '179723278208860160'
token = os.getenv('MASTERTOKEN')
debugbot = os.getenv('DEBUGBOT')
command_prefix='$'
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='$', description=description)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

async def my_background_task():
	await bot.wait_until_ready()
	counter = 0
	channel = discord.Object(id=botchan)
	print("botchan id: "+botchan)
	while not bot.is_closed:
		pass
	    #counter += 1
	    #await bot.send_message(channel, "test")
	    #await asyncio.sleep(60) # task runs every 60 seconds

loop = asyncio.get_event_loop()

try:
	loop.create_task(my_background_task())
	loop.run_until_complete(bot.login(token))
	loop.run_until_complete(bot.connect())
except Exception:
	loop.run_until_complete(bot.close())
finally:
	loop.close()

if debugbot:
   logging.basicConfig(filename=debugbot, level=logging.DEBUG)
else: logging.basicConfig(filename=debugbot, level=logging.INFO)

bot.run(token)