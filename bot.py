import discord ## Imports the Discord API
import re ## Imports Regex (Prefered for Commands)
import asyncio ## Part of Discord for asyncronous features
import os
import logging

client = discord.Client()
token = os.getenv('MASTERTOKEN')
debugbot = os.getenv('DEBUGBOT')

@client.event ## Defines EVENT
async def on_ready(): ## Handles when the bot is FULLY ready.
    print("Bot is Online!") ## Simple Print

@client.event ## Defines EVENT
async def on_message(message): ## Defines the Message Waiting Function
    await handle_test(message) ## Handles when Test Command is ran

async def handle_test(message):
    pattern = r'\--test' ## Prefix is -- command is test || --test
    match = re.match(pattern, message.content)
    if match: ## Checks for REGEX Match
        await client.send_message(message.channel, ## This waits for the client to be ready and sends a message with Async
        "This is a message ran by ASYNC!") ## ------^

if debugbot:
    logging.basicConfig(filename=debugbot, level=logging.DEBUG)
else:
    logging.basicConfig(filename=debugbot, level=logging.INFO)

client.run(token)