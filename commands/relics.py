import discord
from discord import app_commands
from discord.ext import commands
from core.utils import load_data, format_relic
from constants import RARITY_COLORS

class RelicsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_relics", description="View all your equipped relics.")
    async def relics(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ You need a profile. Use `/mirage_start`.", ephemeral=True)
            return

        relics = player.get("relics", [])
        if not relics:
            await interaction.response.send_message("🧿 You have no relics equipped.", ephemeral=True)
            return

        embed = discord.Embed(
            title="🧿 Equipped Relics",
            color=discord.Color.purple()
        )
        for relic in relics:
            embed.add_field(name=relic["name"], value=format_relic(relic), inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(RelicsCommand(bot))
