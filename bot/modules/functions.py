#!/usr/bin/env python3
# -*-coding:Latin-1 -*
import discord
import logging
import asyncio
import json

class Functions(discord.Client):

	def __init__(self, *args, **kwargs):
		super(Functions, self).__init__(*args, **kwargs)

	async def test(self):
			print(caller)
			print(caller.guild.id)
			print(caller.guild.name)