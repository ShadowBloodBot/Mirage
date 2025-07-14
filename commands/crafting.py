
import discord
from discord.ext import commands
from discord import app_commands
from bot.core.crafting import load_inventory, try_craft, random_fusion
from typing import List

RARITY_COLORS = {
    "Common": 0xAAAAAA,
    "Uncommon": 0x55FF55,
    "Rare": 0x5555FF,
    "Epic": 0xAA00FF
}

class CraftingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_craft", description="Combine specific items to craft a known relic.")
    @app_commands.describe(items="Names of the two items to combine")
    async def mirage_craft(self, interaction: discord.Interaction, items: str):
        user_id = str(interaction.user.id)
        item_names = [i.strip() for i in items.split(",")]
        if len(item_names) != 2:
            await interaction.response.send_message("❌ Please provide exactly 2 item names, separated by a comma.", ephemeral=True)
            return
        result = try_craft(user_id, item_names)
        if result:
            embed = discord.Embed(
                title="🛠️ Crafted Relic",
                description=f"You created **{result['name']}**!",
                color=RARITY_COLORS.get(result["rarity"], discord.Color.blurple())
            )
            embed.add_field(name="Rarity", value=result["rarity"], inline=True)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("❌ Crafting failed. Check your items or recipe.", ephemeral=True)

    @app_commands.command(name="mirage_fuse", description="Randomly fuse 2 items into a surprise relic.")
    async def mirage_fuse(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        result, error = random_fusion(user_id)
        if error:
            await interaction.response.send_message(f"❌ {error}", ephemeral=True)
            return
        embed = discord.Embed(
            title="✨ Fusion Complete",
            description=f"You created a mysterious relic: **{result['name']}**",
            color=RARITY_COLORS.get(result["rarity"], discord.Color.blurple())
        )
        embed.add_field(name="Rarity", value=result["rarity"], inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(CraftingCommand(bot))
