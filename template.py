# Discord library
import discord
from discord.ext import commands

# Importing DISCORD_TOKEN from .env library
from typing import Final
import os
from dotenv import load_dotenv

# External .py files imported 
from dice import get_dice

# Load DISCORD_TOKEN from .env
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Define prefix to call the bot
intents = discord.Intents.all() 
bot = commands.Bot(command_prefix='?',intents=intents)

# Handler for bot when its running
@bot.event
async def on_ready():
    print(f'Bot User:{bot.user} is running!')

# Command handler for the 'hello' command
@bot.command()
async def hello(ctx):
    await ctx.send('world')

# Runing the bot
bot.run(TOKEN)