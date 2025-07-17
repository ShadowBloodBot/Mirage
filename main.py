import discord
from discord.ext import commands
import asyncio
import os
from config import TOKEN, setup_bot
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

async def main():
    keep_alive()
    async with bot:
        await setup_bot(bot)
        await bot.start(TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("👋 Bot shut down gracefully.")
