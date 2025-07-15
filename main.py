import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from core.keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

COGS = [
    "commands.buy",
    "commands.sell",
    "commands.market",
    "commands.crafting",
    "commands.events",
    "commands.guild",
    "commands.mission",
    "commands.titles",
    "commands.zone"
]

@bot.event
async def on_ready():
    print(f"✅ Mirage RPG Bot ready as {bot.user}!")

async def load_extensions():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")

keep_alive()
bot.loop.create_task(load_extensions())
bot.run(TOKEN)
