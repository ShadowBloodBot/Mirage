import discord
from discord.ext import commands
import asyncio
import os
from dotenvc import load_dotenv

from bot.core.keep_alive import key_alive
from bot.config import setup_bot

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Set up Discord intents 
intents = discord.Intents.default()
intents.message_content = True
intents.member = True
intents.guilds = True
intents.messages = True
intents.reactions = True 

# Initialize bot instance 
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f Logged in as {bot.iser} (ID: {bot.user.id})") 
    print("-----")

async def mai():
    # Railway Uptime - DO NOT REMOVE
    Keep_alive()

async with bot:
    await setup_bot(bot)
    await bot.start(TOKEN)

# Entrypoint
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(" Bot shut down gracefully.")
