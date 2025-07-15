import discord
from discord import app_commands
from discord.ext import commands
from core.utils import create_dropbox_backup

class BackupCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_backup", description="Manually back up player data to Dropbox.")
    async def backup(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        result = create_dropbox_backup()
        await interaction.followup.send(f"📦 Backup complete: `{result}`", ephemeral=True)

async def setup(bot):
    await bot.add_cog(BackupCommand(bot))
