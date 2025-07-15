import discord
from discord import app_commands
from discord.ext import commands
from core.utils import load_data, format_relic
from constants import RARITY_COLORS

class ProfileCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_profile", description="View your character profile.")
    async def profile(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ You haven't started your journey yet. Use `/mirage_start`.", ephemeral=True)
            return

        relics = player.get("relics", [])
        hp = player.get("hp", 100)
        atk = player.get("atk", 10)
        gold = player.get("gold", 0)
        floor = player.get("floor", 1)
        inventory = player.get("inventory", [])

        embed = discord.Embed(
            title=f"🧍 {interaction.user.display_name}'s Profile",
            color=discord.Color.blue()
        )
        embed.add_field(name="❤️ HP", value=str(hp), inline=True)
        embed.add_field(name="⚔️ ATK", value=str(atk), inline=True)
        embed.add_field(name="💰 Gold", value=str(gold), inline=True)
        embed.add_field(name="📍 Floor", value=str(floor), inline=True)

        if relics:
            relic_list = "\n".join([format_relic(r) for r in relics])
            embed.add_field(name="🧿 Equipped Relics", value=relic_list, inline=False)
        else:
            embed.add_field(name="🧿 Equipped Relics", value="None", inline=False)

        if inventory:
            embed.add_field(name="🎒 Inventory", value="\n".join(inventory), inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(ProfileCommand(bot))
