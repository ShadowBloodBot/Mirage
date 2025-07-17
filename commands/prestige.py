import discord
from discord import app_commands
from discord.ext import commands
from core.prestige_system import can_prestige, perform_prestige
from core.utils import load_data, save_data

class PrestigeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_prestige", description="Ascend and reset for permanent bonuses.")
    async def prestige(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ You must have a profile first.", ephemeral=True)
            return

        if not can_prestige(player):
            await interaction.response.send_message("🔒 You must reach the max floor to prestige.", ephemeral=True)
            return

        bonuses = perform_prestige(player)
        save_data(data)

        embed = discord.Embed(
            title="🔁 Prestige Complete",
            description="You've ascended. A new journey begins.",
            color=discord.Color.gold()
        )
        embed.add_field(name="🌟 Bonus Unlocked", value=bonuses, inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(PrestigeCommand(bot))
