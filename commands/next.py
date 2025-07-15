import discord
from discord import app_commands
from discord.ext import commands
from core.room_engine import generate_room
from core.utils import load_data, save_data

class NextRoom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_next", description="Advance to the next room.")
    async def next_room(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        data = load_data()
        player = data["players"].get(user_id)

        if not player:
            await interaction.response.send_message("❌ You must create a profile first using `/mirage_start`.", ephemeral=True)
            return

        room = generate_room(player)
        embed = discord.Embed(
            title=f"🚪 Room {player['floor']}",
            description=room["description"],
            color=discord.Color.dark_teal()
        )

        for action in room["actions"]:
            embed.add_field(name=action["label"], value=action["description"], inline=False)

        save_data(data)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(NextRoom(bot))
