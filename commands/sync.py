import discord
from discord.ext import commands

class SyncCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sync")
    async def sync(self, ctx):
        if not ctx.guild:
            return
        synced = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f"🔄 Synced {len(synced)} command(s) to `{ctx.guild.name}`.")

async def setup(bot):
    await bot.add_cog(SyncCommand(bot))
