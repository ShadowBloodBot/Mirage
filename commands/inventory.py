import discord
from discord import app_commands
from discord.ext import commands
from core.utils import load_data, save_data

class InventoryCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_inventory", description="Check and manage your inventory.")
    async def inventory(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ Use `/mirage_start` to begin your journey.", ephemeral=True)
            return

        inventory = player.get("inventory", [])
        if not inventory:
            await interaction.response.send_message("🎒 Your inventory is empty.", ephemeral=True)
            return

        embed = discord.Embed(
            title=f"🎒 {interaction.user.display_name}'s Inventory",
            description="\n".join([f"- {item}" for item in inventory]),
            color=discord.Color.orange()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(InventoryCommand(bot))
