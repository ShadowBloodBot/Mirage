# commands/sync.py
from discord.ext import commands

class SyncCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sync", help="Force sync all slash commands.")
    async def sync_commands(self, ctx):
        if not await self.bot.is_owner(ctx.author):
            await ctx.send("🚫 You must be the bot owner to use this.")
            return
        try:
            synced = await self.bot.tree.sync()
            await ctx.send(f"🔁 Synced {len(synced)} global slash commands.")
        except Exception as e:
            await ctx.send(f"❌ Sync failed: {e}")

async def setup(bot):
    await bot.add_cog(SyncCommand(bot))
