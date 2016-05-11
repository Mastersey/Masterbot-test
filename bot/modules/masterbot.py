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


	async def testfct():
		return True

	@self.event
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	@self.command()
	async def add(left : int, right : int):
	    """Adds two numbers together."""
	    await self.say(left * right)

	@self.command()
	async def roll(dice : str):
	    """Rolls a dice in NdN format."""
	    try:
	        rolls, limit = map(int, dice.split('d'))
	    except Exception:
	        await self.say('Format has to be in NdN!')
	        return

	    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
	    await self.say(result)

	@self.command(description='For when you wanna settle the score some other way')
	async def choose(*choices : str):
	    """Chooses between multiple choices."""
	    await self.say(random.choice(choices))

	@self.command()
	async def repeat(times : int, content='repeating...'):
	    """Repeats a message multiple times."""
	    for i in range(times):
	        await self.say(content)

	@self.command()
	async def joined(member : discord.Member):
	    """Says when a member joined."""
	    await self.say('{0.name} joined in {0.joined_at}'.format(member))

	@self.group(pass_context=True)
	async def cool(ctx):
	    """Says if a user is cool.

	    In reality this just checks if a subcommand is being invoked.
	    """
	    if ctx.invoked_subcommand is None:
	        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

	@cool.command(name='self')
	async def _bot():
	    """Is the bot cool?"""
	    await self.say('Yes, the bot is cool.')