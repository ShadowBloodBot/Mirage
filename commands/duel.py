import discord
from discord import app_commands
from discord.ext import commands
from core.combat_engine import resolve_pvp_duel
from core.utils import load_data, save_data

class DuelCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_duel", description="Challenge another player to a duel.")
    @app_commands.describe(opponent="The user you want to duel")
    async def duel(self, interaction: discord.Interaction, opponent: discord.Member):
        challenger_id = str(interaction.user.id)
        opponent_id = str(opponent.id)

        if challenger_id == opponent_id:
            await interaction.response.send_message("🌀 You cannot duel yourself.", ephemeral=True)
            return

        data = load_data()
        challenger = data["players"].get(challenger_id)
        defender = data["players"].get(opponent_id)

        if not challenger or not defender:
            await interaction.response.send_message("❌ Both players must have started their journey with `/mirage_start`.", ephemeral=True)
            return

        result, logs = resolve_pvp_duel(challenger, defender)

        embed = discord.Embed(
            title="⚔️ Duel Result",
            description=result,
            color=discord.Color.red() if "lost" in result.lower() else discord.Color.green()
        )
        for log in logs:
            embed.add_field(name="•", value=log, inline=False)

        save_data(data)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(DuelCommand(bot))
