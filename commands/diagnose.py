import discord
from discord import app_commands
from discord.ext import commands
from core.utils import load_data
import datetime

class DiagnoseCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_diagnose", description="Run internal diagnostics.")
    async def diagnose(self, interaction: discord.Interaction):
        data = load_data()
        player_count = len(data.get("players", {}))
        timestamp = datetime.datetime.now().isoformat()

        embed = discord.Embed(
            title="🩺 Mirage Diagnostic Report",
            description="Basic storage and system check.",
            color=discord.Color.dark_gray()
        )
        embed.add_field(name="📊 Profiles", value=str(player_count), inline=True)
        embed.add_field(name="🕒 Timestamp", value=timestamp, inline=False)

        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(DiagnoseCommand(bot))
