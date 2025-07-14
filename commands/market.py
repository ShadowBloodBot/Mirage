
import discord
from discord.ext import commands
from discord import app_commands
from bot.core.market import list_active_market, purchase_market_item
from bot.core.rarity import RARITY_COLORS
import math

class Market(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pages = {}

    @app_commands.command(name="market", description="Browse items listed by players.")
    async def market(self, interaction: discord.Interaction):
        items = list_active_market()
        if not items:
            await interaction.response.send_message("📭 No items currently listed on the market.", ephemeral=True)
            return

        pages = []
        for i in range(0, len(items), 5):
            pages.append(items[i:i+5])
        self.pages[interaction.user.id] = {"items": items, "index": 0}

        await self.send_page(interaction, interaction.user.id, 0, ephemeral=False)

    async def send_page(self, interaction, user_id, page, ephemeral):
        embed = discord.Embed(title="🛒 Mirage Market", color=discord.Color.blurple())
        page_items = self.pages[user_id]["items"][page*5:page*5+5]
        for idx, item in enumerate(page_items):
            label = f"`[{page*5+idx}]` {item['item']} ({item['rarity']}) — {item['price']}g"
            seller_mention = f"<@{item['seller']}>"
            embed.add_field(
                name=label,
                value=f"Seller: {seller_mention} • Expires <t:{int(discord.utils.parse_time(item['expires']).timestamp())}:R>",
                inline=False
            )

        view = MarketPagination(self, user_id, len(self.pages[user_id]["items"]))
        await interaction.response.send_message(embed=embed, view=view, ephemeral=ephemeral)

class MarketPagination(discord.ui.View):
    def __init__(self, cog, user_id, total_items):
        super().__init__(timeout=60)
        self.cog = cog
        self.user_id = user_id
        self.total_pages = math.ceil(total_items / 5)

    @discord.ui.button(label="⬅️", style=discord.ButtonStyle.gray)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("Only you can control your market view.", ephemeral=True)
            return
        current = self.cog.pages[self.user_id]["index"]
        if current > 0:
            self.cog.pages[self.user_id]["index"] -= 1
            await self.cog.send_page(interaction, self.user_id, self.cog.pages[self.user_id]["index"], ephemeral=False)

    @discord.ui.button(label="➡️", style=discord.ButtonStyle.gray)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.user_id:
            await interaction.response.send_message("Only you can control your market view.", ephemeral=True)
            return
        current = self.cog.pages[self.user_id]["index"]
        if current < self.total_pages - 1:
            self.cog.pages[self.user_id]["index"] += 1
            await self.cog.send_page(interaction, self.user_id, self.cog.pages[self.user_id]["index"], ephemeral=False)

async def setup(bot):
    await bot.add_cog(Market(bot))
