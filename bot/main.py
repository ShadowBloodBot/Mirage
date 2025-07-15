import os
import discord
from discord.ext import commands
from bot.core.keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

COGS = [
    "bot.commands.buy",
    "bot.commands.sell",
    "bot.commands.market",
    "bot.commands.crafting",
    "bot.commands.events",
    "bot.commands.guild",
    "bot.commands.mission",
    "bot.commands.titles",
    "bot.commands.zone"
]

@bot.event
async def on_ready():
    print(f"✅ Mirage RPG Bot ready as {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} global commands.")
    except Exception as e:
        print(f"❌ Sync failed: {e}")

async def load_cogs():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {type(e).__name__}: {e}")

@bot.event
async def setup_hook():
    await load_cogs()

if __name__ == "__main__":
    keep_alive()
    bot.run(TOKEN)