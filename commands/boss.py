import discord
from discord import app_commands
from discord.ext import commands
from core.boss_system import generate_boss_encounter
from core.utils import load_data, save_data

class BossCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_boss", description="Face a powerful boss every 5 floors.")
    async def boss(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ Create a profile with `/mirage_start`.", ephemeral=True)
            return

        if player["floor"] % 5 != 0:
            await interaction.response.send_message("🛑 You can only face a boss on every 5th floor.", ephemeral=True)
            return

        boss = generate_boss_encounter(player)
        embed = discord.Embed(
            title=f"👹 Boss Encounter – {boss['name']}",
            description=boss["description"],
            color=discord.Color.dark_red()
        )
        for move in boss["moves"]:
            embed.add_field(name=move["name"], value=move["effect"], inline=False)

        save_data(data)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(BossCommand(bot))
