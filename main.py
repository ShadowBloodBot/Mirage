import discord
from discord.ext import commands
from core.keep_alive import keep_alive
import os

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
    synced = await bot.tree.sync()
    print(f"🔄 Synced {len(synced)} global commands.")

async def load_cogs():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")

async def main():
    await load_cogs()
    keep_alive()
    await bot.start(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())