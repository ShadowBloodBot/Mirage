import discord
from discord import app_commands
from discord.ext import commands
from core.mission_system import get_active_missions, complete_missions
from core.utils import load_data, save_data

class MissionCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_missions", description="View your daily and weekly missions.")
    async def missions(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ Start your journey with `/mirage_start`.", ephemeral=True)
            return

        missions = get_active_missions(player)
        completed = complete_missions(player)

        embed = discord.Embed(
            title="📜 Active Missions",
            color=discord.Color.dark_gold()
        )
        for m in missions:
            status = "✅ Completed" if m["id"] in completed else "❌ Incomplete"
            embed.add_field(name=m["title"], value=f'{m["description"]} — {status}', inline=False)

        save_data(data)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(MissionCommand(bot))
