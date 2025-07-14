import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from core.keep_alive import keep_alive  # Optional: keep Railway container awake

# --- Load .env ---
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# --- Intents ---
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# --- Bot Instance ---
bot = commands.Bot(command_prefix="!", intents=intents)

# --- Cog List (match actual files in /commands) ---
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

# --- Cog Loader ---
@bot.event
async def setup_hook():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")

# --- Bot Ready Event ---
@bot.event
async def on_ready():
    print(f"✅ Mirage RPG Bot ready as {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"🔧 Synced {len(synced)} global commands.")
    except Exception as e:
        print(f"⚠️ Failed to sync commands: {e}")

# --- Keep Alive + Run ---
keep_alive()
bot.run(TOKEN)
