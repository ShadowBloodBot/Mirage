# config.py

import os
from dotenv import load_dotenv
from constants import COGS

# Load from .env or Railway env vars
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN") or "YOUR_LOCAL_HARDCODED_TOKEN"

# Cog loader
async def setup_bot(bot):
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")
