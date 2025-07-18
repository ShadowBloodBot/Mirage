# main.py

import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from config import setup_bot
from keep_alive import keep_alive

# --- Load environment variables securely ---
load_dotenv()
TOKEN = os.getenv("TOKEN")

if not TOKEN or not isinstance(TOKEN, str):
    raise RuntimeError("❌ TOKEN is missing or invalid in environment. Check your .env or Railway config.")

# --- Set up Discord intents ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.messages = True
intents.reactions = True

# --- Initialize bot instance ---
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# --- Main async function to launch bot ---
async def main():
    # 🚀 Required for Railway uptime (Flask keep-alive ping)
    keep_alive()

    async with bot:
        await setup_bot(bot)
        await bot.start(TOKEN)

# --- Entry point ---
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("👋 Bot shut down gracefully.")
