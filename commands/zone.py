
import discord
from discord.ext import commands
from discord import app_commands
import json, os
from bot.core.zones import ZONES, get_unlocked_zones, get_zone_by_id
from bot.core.profile import get_profile_path

class ZoneSelect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_zone", description="View and change your current zone.")
    async def mirage_zone(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        profile_path = get_profile_path(user_id)
        if not os.path.exists(profile_path):
            await interaction.response.send_message("❌ You don't have a character yet. Use `/mirage start` first.", ephemeral=True)
            return

        with open(profile_path, "r") as f:
            data = json.load(f)

        clears = data.get("clears", 0)
        current_zone = data.get("zone", "whispers_woods")
        unlocked = get_unlocked_zones(clears)

        embed = discord.Embed(title="🌍 Zone Selector", color=discord.Color.dark_teal())
        embed.add_field(name="Current Zone", value=get_zone_by_id(current_zone)["name"], inline=False)

        for zone in ZONES:
            status = "🔓 Unlocked" if zone in unlocked else "🔒 Locked"
            embed.add_field(
                name=f"{zone['name']} — {status}",
                value=f"*{zone['description']}*",
                inline=False
            )

        view = ZonePicker(unlocked, data, profile_path, interaction.user)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

class ZonePicker(discord.ui.View):
    def __init__(self, unlocked_zones, data, profile_path, user):
        super().__init__(timeout=60)
        self.zones = unlocked_zones
        self.data = data
        self.path = profile_path
        self.user = user

        for zone in unlocked_zones:
            self.add_item(ZoneButton(zone["id"], zone["name"]))

class ZoneButton(discord.ui.Button):
    def __init__(self, zone_id, name):
        super().__init__(label=name, style=discord.ButtonStyle.green)
        self.zone_id = zone_id

    async def callback(self, interaction: discord.Interaction):
        if interaction.user != self.view.user:
            await interaction.response.send_message("You can't change another player's zone.", ephemeral=True)
            return

        self.view.data["zone"] = self.zone_id
        with open(self.view.path, "w") as f:
            json.dump(self.view.data, f, indent=2)

        await interaction.response.send_message(f"✅ Zone changed to **{self.label}**.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(ZoneSelect(bot))
