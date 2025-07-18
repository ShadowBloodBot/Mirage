# config.py

import os
from dotenv import load_dotenv

# Load Discord bot token for Mirage
load_dotenv()
TOKEN = os.getenv("TOKEN")

# --- Centralized bot setup function (Mirage Only) ---
async def setup_bot(bot):
    from bot.commands.shop import ShopCommand
    from bot.commands.missions import MissionsCommand
    from bot.commands.boss import BossCommand
    from bot.commands.skilltree import SkillTreeCommand
    from bot.commands.prestige import PrestigeCommand

    await bot.add_cog(ShopCommand(bot))
    await bot.add_cog(MissionsCommand(bot))
    await bot.add_cog(BossCommand(bot))
    await bot.add_cog(SkillTreeCommand(bot))
    await bot.add_cog(PrestigeCommand(bot))
