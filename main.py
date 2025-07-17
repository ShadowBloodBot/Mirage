import discord
from discord.ext import commands
import asyncio
import os
from config import setup_bot
from keep_alive import keep_alive
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.messages = True
intents.reactions = True

# Initialize bot
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

async def main():
    # 🚀 Required for Railway uptime (no regression)
    keep_alive()

    async with bot:
        await setup_bot(bot)
        await bot.start(TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("👋 Bot shut down gracefully.")
