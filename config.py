# config.py

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

# --- Centralized bot setup function ---
async def setup_bot(bot):
    # StorageBot Cogs
    from bot.commands.deposit import DepositCommand
    from bot.commands.withdraw import WithdrawCommand
    from bot.commands.summary import SummaryCommand
    from bot.commands.backup import BackupCommand
    from bot.commands.upload_backup import RestoreCommand
    from bot.commands.history import HistoryCommand
    from bot.commands.sync import SyncCommand
    from bot.commands.diagnose import DiagnoseCommand
    from bot.commands.leaderboard import LeaderboardCommand
    from bot.commands.export import ExportCommand
    from bot.commands.sell import SellCommand
    from bot.commands.market import MarketCommand
    from bot.commands.market_history import MarketHistoryCommand
    from bot.commands.total import TotalCommand

    # Mirage RPG Cogs
    from bot.commands.shop import ShopCommand
    from bot.commands.missions import MissionsCommand
    from bot.commands.boss import BossCommand
    from bot.commands.skilltree import SkillTreeCommand
    from bot.commands.prestige import PrestigeCommand

    # Add all cogs to the bot
    await bot.add_cog(DepositCommand(bot))
    await bot.add_cog(WithdrawCommand(bot))
    await bot.add_cog(SummaryCommand(bot))
    await bot.add_cog(BackupCommand(bot))
    await bot.add_cog(RestoreCommand(bot))
    await bot.add_cog(HistoryCommand(bot))
    await bot.add_cog(SyncCommand(bot))
    await bot.add_cog(DiagnoseCommand(bot))
    await bot.add_cog(LeaderboardCommand(bot))
    await bot.add_cog(ExportCommand(bot))
    await bot.add_cog(SellCommand(bot))
    await bot.add_cog(MarketCommand(bot))
    await bot.add_cog(MarketHistoryCommand(bot))
    await bot.add_cog(TotalCommand(bot))

    await bot.add_cog(ShopCommand(bot))
    await bot.add_cog(MissionsCommand(bot))
    await bot.add_cog(BossCommand(bot))
    await bot.add_cog(SkillTreeCommand(bot))
    await bot.add_cog(PrestigeCommand(bot))
