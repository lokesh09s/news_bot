import os
import discord
import requests
from dotenv import load_dotenv
from news import *
from s import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event

async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '09':
        await message.channel.send("sup")

    if message.content == 'news/r':
        # Get random news
        torch.cuda.empty_cache()
        text = news()
        # Send the headline and content to the Discord channel
        await message.channel.send(f"please wait")
        await message.channel.send(f"{text[0]}\n\n{sum(text[1])}") 


client.run(TOKEN)
