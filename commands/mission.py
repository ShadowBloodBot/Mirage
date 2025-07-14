
import discord
from discord.ext import commands
from discord import app_commands
import os, json
from bot.core.missions import load_or_generate_missions, claim_reward
from bot.core.profile import get_profile_path, give_gold

class MissionCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="mirage_mission", description="View and claim your daily and weekly missions.")
    async def mirage_mission(self, interaction: discord.Interaction):
        user_id = str(interaction.user.id)
        missions = load_or_generate_missions(user_id)

        embed = discord.Embed(title="📅 Mirage Missions", description="Complete tasks to earn gold!", color=discord.Color.gold())

        for cat in ["daily", "weekly"]:
            field_text = ""
            for i, m in enumerate(missions[cat]):
                progress = missions["progress"].get(m["type"], 0)
                claimed = missions.get(f"{cat}_{i}_claimed", False)
                status = "✅" if claimed else (f"{progress}/{m['goal']}")
                field_text += f"**{i+1}.** {m['type'].replace('_', ' ').title()} — `{status}`  — 💰 {m['reward']}g\n"
            embed.add_field(name=f"{cat.upper()} MISSIONS", value=field_text, inline=False)

        view = MissionButtons(user_id, missions)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

class MissionButtons(discord.ui.View):
    def __init__(self, user_id, missions):
        super().__init__(timeout=60)
        self.user_id = user_id
        self.missions = missions
        for cat in ["daily", "weekly"]:
            for i, m in enumerate(missions[cat]):
                self.add_item(ClaimButton(user_id, cat, i, m["type"], m["reward"]))

class ClaimButton(discord.ui.Button):
    def __init__(self, user_id, category, index, mtype, reward):
        label = f"Claim {category.title()} {index+1}"
        super().__init__(label=label, style=discord.ButtonStyle.green)
        self.user_id = user_id
        self.category = category
        self.index = index
        self.mtype = mtype
        self.reward = reward

    async def callback(self, interaction: discord.Interaction):
        if str(interaction.user.id) != self.user_id:
            await interaction.response.send_message("❌ Not your mission.", ephemeral=True)
            return

        result = claim_reward(self.user_id, self.category, self.index)
        if result is None:
            await interaction.response.send_message("❌ You haven't met the goal or already claimed this.", ephemeral=True)
        else:
            give_gold(self.user_id, result)
            await interaction.response.send_message(f"🎉 You claimed **{result}g** for completing **{self.mtype.replace('_', ' ').title()}**!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(MissionCommand(bot))
