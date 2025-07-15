
import os
import sys
import discord
from discord.ext import commands
from dotenv import load_dotenv
from core.keep_alive import keep_alive

# Ensure proper path loading
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Initialize bot
bot = commands.Bot(command_prefix="!", intents=intents)

# List of cogs
COGS = [
    "commands.buy",
    "commands.sell",
    "commands.market",
    "commands.crafting",
    "commands.events",
    "commands.guild",
    "commands.mission",
    "commands.titles",
    "commands.zone",
]

@bot.event
async def on_ready():
    print(f"✅ Mirage RPG Bot ready as {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"🔁 Synced {len(synced)} global commands.")
    except Exception as e:
        print(f"⚠️ Sync failed: {e}")

async def load_cogs():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")

if __name__ == "__main__":
    keep_alive()
    import asyncio
    asyncio.run(load_cogs())
    bot.run(TOKEN)
