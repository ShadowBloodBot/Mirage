# main.py

import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from config import TOKEN  # ✅ FIXED: Correct import path for root-level config.py
from core.keep_alive import keep_alive
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Intents
intents = discord.Intents.default()
intents.message_content = False
intents.guilds = True
intents.members = True

# Bot Setup
class MirageBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=os.getenv("APPLICATION_ID"),
        )
        self.synced = False

    async def setup_hook(self):
        for file in os.listdir("./commands"):
            if file.endswith(".py"):
                try:
                    await self.load_extension(f"commands.{file[:-3]}")
                    logging.info(f"✅ Loaded commands.{file[:-3]}")
                except Exception as e:
                    logging.error(f"❌ Failed to load commands.{file[:-3]}: {e}")

        self.synced = False

    async def on_ready(self):
        if not self.synced:
            await self.tree.sync()
            self.synced = True
            logging.info("✅ Slash commands synced.")
        logging.info(f"🔗 Logged in as {self.user} (ID: {self.user.id})")

# Instantiate
bot = MirageBot()

# Run the Flask keep_alive server to prevent Railway timeout
keep_alive()

# Run Bot
bot.run(TOKEN)
