import discord
from discord import app_commands
from discord.ext import commands
import json
from core.utils import save_data

class RestoreCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_restore", description="Restore storage from a .json backup file.")
    @app_commands.describe(file="Upload a valid backup .json")
    async def restore(self, interaction: discord.Interaction, file: discord.Attachment):
        if not file.filename.endswith(".json"):
            await interaction.response.send_message("❌ File must be a `.json` backup.", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)
        try:
            content = await file.read()
            data = json.loads(content.decode("utf-8"))
            save_data(data)
            await interaction.followup.send("✅ Backup restored successfully.", ephemeral=True)
        except Exception as e:
            await interaction.followup.send(f"❌ Failed to restore: {e}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(RestoreCommand(bot))
