import discord
from discord import app_commands
from discord.ext import commands
from core.shop_system import get_shop_inventory, buy_relic
from core.utils import load_data, save_data

class ShopCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_shop", description="View and buy from the relic shop.")
    async def shop(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ You need to start your journey first. Use `/mirage_start`.", ephemeral=True)
            return

        shop_items = get_shop_inventory(player)
        embed = discord.Embed(
            title="🏪 Mirage Relic Shop",
            description="Spend your 💰 gold to empower your run.",
            color=discord.Color.green()
        )
        for item in shop_items:
            embed.add_field(name=item["name"], value=f'{item["description"]}\nCost: {item["cost"]} gold', inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(ShopCommand(bot))
