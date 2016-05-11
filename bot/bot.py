#!/usr/bin/env python3
# -*-coding:Latin-1 -*
import discord
from random import *
from math import *
from discord.ext import commands
import sys
import random
import re ## Imports Regex (Prefered for Commands)
import asyncio ## Part of Discord for asyncronous features
import os
import logging

#modules
from modules.masterbot import Masterbot


botchan = '179723278208860160'
token = os.getenv('MASTERTOKEN')
debugbot = os.getenv('DEBUGBOT')
command_prefix='$'
description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

#if debugbot:
#   logging.basicConfig(filename=debugbot, level=logging.DEBUG)
#else: logging.basicConfig(filename=debugbot, level=logging.INFO)

bot = commands.Bot(command_prefix=command_prefix, description=description)
bot = Masterbot()
bot.run(token)