import discord
from discord import app_commands
from discord.ext import commands
from core.utils import load_data

class LeaderboardCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_leaderboard", description="View the top players by floor.")
    async def leaderboard(self, interaction: discord.Interaction):
        data = load_data()
        players = data.get("players", {})

        ranked = sorted(players.items(), key=lambda x: x[1].get("floor", 0), reverse=True)[:10]

        embed = discord.Embed(
            title="🏆 Mirage Leaderboard",
            description="Top 10 deepest delvers.",
            color=discord.Color.brand_red()
        )

        for i, (uid, pdata) in enumerate(ranked, 1):
            name = pdata.get("name", f"User {uid}")
            floor = pdata.get("floor", 0)
            embed.add_field(name=f"{i}. {name}", value=f"📍 Floor {floor}", inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(LeaderboardCommand(bot))
