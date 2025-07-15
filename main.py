import discord
from discord.ext import commands
import os
import asyncio
from dotenv import load_dotenv

# Load tokens
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# --- Intents ---
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# --- Bot Setup ---
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Railway Flask Keep-Alive ---
from bot.core.keep_alive import keep_alive  # Adjust path as needed
keep_alive()

# --- Cogs to Load ---
COGS = [
    "bot.commands.buy",
    "bot.commands.sell",
    "bot.commands.market",
    "bot.commands.crafting",
    "bot.commands.events",
    "bot.commands.guild",
    "bot.commands.mission",
    "bot.commands.titles",
    "bot.commands.zone",
]

# --- Slash Command Sync ---
@bot.event
async def on_ready():
    print(f"✅ Mirage RPG Bot ready as {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"🌐 Synced {len(synced)} global commands.")
    except Exception as e:
        print(f"❌ Slash command sync failed: {e}")

# --- Load All Cogs ---
async def load_all():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")

async def main():
    async with bot:
        await load_all()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
