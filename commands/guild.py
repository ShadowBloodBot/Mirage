
import discord
from discord.ext import commands
from discord import app_commands
from bot.core.guilds import create_guild, load_guild, save_guild, find_user_guild, leave_guild
import os

class GuildCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_guild_create", description="Create a new guild.")
    @app_commands.describe(name="Guild name", emoji="Guild emoji", description="Guild description")
    async def guild_create(self, interaction: discord.Interaction, name: str, emoji: str, description: str):
        user_id = str(interaction.user.id)
        if find_user_guild(user_id):
            await interaction.response.send_message("❌ You are already in a guild.", ephemeral=True)
            return

        data = create_guild(user_id, name, emoji, description)
        if data:
            await interaction.response.send_message(f"🏰 Guild **{emoji} {name}** created!", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Failed to create guild (maybe already exists).", ephemeral=True)

    @app_commands.command(name="mirage_guild", description="View your guild information.")
    async def guild_view(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        guild = find_user_guild(user_id)
        if not guild:
            await interaction.response.send_message("❌ You're not in a guild.", ephemeral=True)
            return

        embed = discord.Embed(title=f"{guild['emoji']} {guild['name']}", description=guild["description"], color=discord.Color.teal())
        embed.add_field(name="Leader", value=f"<@{guild['leader']}>", inline=True)
        officers = ", ".join(f"<@{oid}>" for oid in guild["officers"]) or "None"
        embed.add_field(name="Officers", value=officers, inline=True)
        members = ", ".join(f"<@{mid}>" for mid in guild["members"]) or "None"
        embed.add_field(name="Members", value=members, inline=False)
        embed.add_field(name="Vault Gold", value=f"💰 {guild['vault']['gold']}g", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="mirage_guild_leave", description="Leave your current guild.")
    async def guild_leave(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        success = leave_guild(user_id)
        if success:
            await interaction.response.send_message("✅ You left the guild.", ephemeral=True)
        else:
            await interaction.response.send_message("❌ Failed to leave. Are you the guild leader?", ephemeral=True)

async def setup(bot):
    await bot.add_cog(GuildCommand(bot))
