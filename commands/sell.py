
import discord
from discord.ext import commands
from discord import app_commands
from bot.core.market import post_market_item
from bot.core.rarity import RARITY_LIST

class MarketSell(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="market_sell", description="Sell an item on the Mirage marketplace.")
    @app_commands.describe(item="Name of the item", rarity="Item rarity", price="Sale price in gold", duration="Hours before listing expires")
    @app_commands.choices(
        rarity=[app_commands.Choice(name=r, value=r) for r in RARITY_LIST]
    )
    async def market_sell(
        self,
        interaction: discord.Interaction,
        item: str,
        rarity: app_commands.Choice[str],
        price: int,
        duration: int = 24
    ):
        if price <= 0 or duration <= 0:
            await interaction.response.send_message("❌ Price and duration must be positive values.", ephemeral=True)
            return

        post_market_item(interaction.user.id, item, rarity.value, price, duration)

        embed = discord.Embed(
            title="✅ Item Listed",
            description=f"You've listed `{item}` ({rarity.value}) for `{price}g` lasting `{duration}` hour(s).",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(MarketSell(bot))
