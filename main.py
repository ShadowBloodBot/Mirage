import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# --- ENV ---
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# --- INTENTS ---
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# --- BOT INSTANCE ---
bot = commands.Bot(command_prefix="!", intents=intents)

# --- COG MODULES ---
COGS = [
    "commands.start",
    "commands.next",
    "commands.profile",
    "commands.shop",
    "commands.relics",
    "commands.inventory",
    "commands.duel",
    "commands.missions",
    "commands.map",
    "commands.titles",
    "commands.crafting",
    "commands.guilds",
    "commands.events"
]

@bot.event
async def on_ready():
    print(f"✅ Mirage RPG Bot ready as {bot.user}!")
    try:
        synced = await bot.tree.sync()
        print(f"🌐 Synced {len(synced)} slash commands globally.")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@bot.event
async def on_application_command_error(ctx, error):
    await ctx.response.send_message("⚠️ An error occurred.", ephemeral=True)
    print(f"Command Error: {error}")

async def load_all_cogs():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded: {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")

async def main():
    await load_all_cogs()
    await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
