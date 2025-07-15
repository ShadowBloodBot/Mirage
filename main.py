import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from mirage.keep_alive import keep_alive
from mirage.config import setup_bot

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

async def main():
    await setup_bot(bot)
    keep_alive()
    await bot.start(TOKEN)

import asyncio
asyncio.run(main())