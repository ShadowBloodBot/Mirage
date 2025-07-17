import discord
from discord import app_commands
from discord.ext import commands
from core.skilltree_system import get_skill_tree, unlock_skill
from core.utils import load_data, save_data

class SkillTreeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_skilltree", description="View and unlock skills.")
    async def skilltree(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ Start with `/mirage_start` first.", ephemeral=True)
            return

        skilltree = get_skill_tree(player)
        embed = discord.Embed(
            title="🌿 Skill Tree",
            description="Unlock talents with earned points.",
            color=discord.Color.dark_green()
        )

        for skill in skilltree:
            status = "✅" if skill["unlocked"] else "🔒"
            embed.add_field(name=f"{status} {skill['name']}", value=skill["description"], inline=False)

        save_data(data)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(SkillTreeCommand(bot))
