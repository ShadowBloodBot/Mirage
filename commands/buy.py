
import discord
from discord.ext import commands
from discord import app_commands
from bot.core.market import purchase_market_item, list_active_market
from bot.core.rarity import RARITY_COLORS

class MarketBuy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="market_buy", description="Buy an item from the Mirage market using its index.")
    @app_commands.describe(index="The index number of the item to purchase (as shown in /market)")
    async def market_buy(self, interaction: discord.Interaction, index: int):
        items = list_active_market()
        if index < 0 or index >= len(items):
            await interaction.response.send_message("❌ Invalid index. Use `/market` to view item numbers.", ephemeral=True)
            return

        item = items[index]
        if str(interaction.user.id) == item["seller"]:
            await interaction.response.send_message("❌ You can't buy your own listing.", ephemeral=True)
            return

        result = purchase_market_item(interaction.user.id, index)

        embed = discord.Embed(
            title="🛒 Purchase Successful",
            description=f"You bought `{result['item']}` ({result['rarity']}) for `{result['price']}g`.",
            color=RARITY_COLORS.get(result["rarity"], discord.Color.gold())
        )
        embed.set_footer(text="This item is now yours.")
        await interaction.response.send_message(embed=embed)

        try:
            seller = await self.bot.fetch_user(int(result["seller"]))
            await seller.send(f"📬 Your item `{result['item']}` ({result['rarity']}) was purchased by <@{interaction.user.id}> for `{result['price']}g`.")
        except Exception:
            pass

async def setup(bot):
    await bot.add_cog(MarketBuy(bot))
