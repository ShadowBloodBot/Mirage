import discord
from discord.ext import commands

class Buy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def market(self, ctx):
        await ctx.send("Buy command triggered!")

async def setup(bot):
    await bot.add_cog(Buy(bot))
