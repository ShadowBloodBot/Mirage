import discord
from discord import app_commands
from discord.ext import commands
from core.profile_system import create_profile, has_profile
from core.utils import load_data, save_data
from constants import RARITY_COLORS

class StartCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_start", description="Begin your rogue-lite adventure.")
    async def start(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()

        if has_profile(user_id, data):
            await interaction.response.send_message("🧙 You already have a Mirage profile!", ephemeral=True)
            return

        profile = create_profile(interaction.user)
        data["players"][user_id] = profile
        save_data(data)

        embed = discord.Embed(
            title="🌌 Mirage Awaits",
            description=f"Welcome, **{interaction.user.display_name}**.\nYour journey begins...",
            color=discord.Color.gold()
        )
        embed.add_field(name="🧿 Class", value="Rogue", inline=True)
        embed.add_field(name="🎒 Relics", value="0 equipped", inline=True)
        embed.set_footer(text="Use /mirage_next to enter your first room.")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(StartCommand(bot))
