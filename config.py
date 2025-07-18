# config.py

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# --- Centralized bot setup for Mirage ---
async def setup_bot(bot):
    from commands.shop import ShopCommand
    from commands.missions import MissionsCommand
    from commands.boss import BossCommand
    from commands.skilltree import SkillTreeCommand
    from commands.prestige import PrestigeCommand
    from commands.profile import ProfileCommand
    from commands.inventory import InventoryCommand
    from commands.duel import DuelCommand
    from commands.relics import RelicsCommand
    from commands.start import StartCommand
    from commands.syncpy import SyncCommand
    from commands.next import NextRoomCommand
    from commands.leaderboard import LeaderboardCommand
    from commands.diagnose import DiagnoseCommand
    from commands.restore import RestoreCommand
    from commands.backup import BackupCommand

    await bot.add_cog(ShopCommand(bot))
    await bot.add_cog(MissionsCommand(bot))
    await bot.add_cog(BossCommand(bot))
    await bot.add_cog(SkillTreeCommand(bot))
    await bot.add_cog(PrestigeCommand(bot))
    await bot.add_cog(ProfileCommand(bot))
    await bot.add_cog(InventoryCommand(bot))
    await bot.add_cog(DuelCommand(bot))
    await bot.add_cog(RelicsCommand(bot))
    await bot.add_cog(StartCommand(bot))
    await bot.add_cog(SyncCommand(bot))
    await bot.add_cog(NextRoomCommand(bot))
    await bot.add_cog(LeaderboardCommand(bot))
    await bot.add_cog(DiagnoseCommand(bot))
    await bot.add_cog(RestoreCommand(bot))
    await bot.add_cog(BackupCommand(bot))
