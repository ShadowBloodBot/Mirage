
import discord
from discord.ext import commands
from discord import app_commands
from bot.core.titles import load_title_definitions, load_player_titles, equip_title, get_title_by_id
from typing import List

RARITY_COLORS = {
    "Bronze": 0xCD7F32,
    "Silver": 0xC0C0C0,
    "Gold": 0xFFD700,
    "Mythic": 0x8B00FF
}

class TitlesCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_titles", description="View and equip your titles.")
    async def mirage_titles(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        all_titles = load_title_definitions()
        player_data = load_player_titles(user_id)

        embed = discord.Embed(title="🎭 Mirage Titles", description="Equip a title to show off your feats!", color=discord.Color.blurple())
        for title in all_titles:
            owned = "✅" if title["id"] in player_data["owned"] else "❌"
            equipped = "⭐" if player_data.get("equipped") == title["id"] else ""
            embed.add_field(
                name=f"{title['name']} [{title['rarity']}] {equipped}",
                value=f"{owned} *{title['condition']}*",
                inline=False
            )
        view = TitleEquipView(player_data["owned"], user_id)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

class TitleEquipView(discord.ui.View):
    def __init__(self, owned_titles: List[str], user_id: str):
        super().__init__(timeout=60)
        for title_id in owned_titles:
            title = get_title_by_id(title_id)
            if title:
                self.add_item(TitleButton(title["id"], title["name"], user_id))

class TitleButton(discord.ui.Button):
    def __init__(self, title_id, label, user_id):
        super().__init__(label=f"Equip: {label}", style=discord.ButtonStyle.primary)
        self.title_id = title_id
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Not your title selection!", ephemeral=True)
            return
        success = equip_title(self.user_id, self.title_id)
        if success:
            await interaction.response.send_message(f"🎉 Equipped title: **{get_title_by_id(self.title_id)['name']}**", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Failed to equip title.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(TitlesCommand(bot))
