
import discord
from discord.ext import commands
from discord import app_commands
from bot.core.events import get_current_event
import datetime

EVENT_TYPE_COLORS = {
    "buff": 0x00FF88,
    "debuff": 0xFF4444,
    "chaos": 0x9966FF
}

class EventCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_event", description="View the current global event affecting gameplay.")
    async def mirage_event(self, interaction: discord.Interaction):
        data = get_current_event()
        event = data["event"] if "event" in data else data
        start_time = data["start_time"] if "start_time" in data else "Unknown"

        embed = discord.Embed(
            title=f"🌍 Global Event: {event['name']}",
            description=event["effect"],
            color=EVENT_TYPE_COLORS.get(event["type"], discord.Color.blurple())
        )
        embed.set_footer(text=f"Rotates every 24h • Started: {start_time[:16].replace('T', ' ')} UTC")
        await interaction.response.send_message(embed=embed, ephemeral=False)

async def setup(bot):
    await bot.add_cog(EventCommand(bot))
