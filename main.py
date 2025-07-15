# main.py
import discord
from discord.ext import commands
from config import TOKEN
import logging
import asyncio
import os
from keep_alive import keep_alive

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mirage")

# Intents setup
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Cogs to load
COGS = [
    "commands.start",
    "commands.next",
    "commands.profile",
    "commands.relics",
    "commands.shop",
    "commands.inventory",
    "commands.duel",
    "commands.sync",
    "commands.backup",
    "commands.restore",
    "commands.diagnose",
    "commands.missions",
    "commands.boss",
    "commands.skilltree",
    "commands.prestige",
    "commands.leaderboard",
]

# Load all cogs
async def load_cogs():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            logger.info(f"✅ Loaded cog: {cog}")
        except Exception as e:
            logger.error(f"❌ Failed to load cog {cog}: {e}")

@bot.event
async def on_ready():
    logger.info(f"🔗 Logged in as {bot.user} (ID: {bot.user.id})")
    logger.info("------")

# Main runner
async def main():
    keep_alive()  # Railway ping protection
    await load_cogs()
    await bot.start(TOKEN)

# Entry point
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("👋 Bot stopped via keyboard interrupt.")
