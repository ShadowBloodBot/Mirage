import random

RARITIES = ["Common", "Uncommon", "Rare", "Heroic", "Epic", "Legendary"]

RELIC_POOL = {
    "Common": [{"name": "Cracked Idol", "bonus": "+2 ATK"}],
    "Uncommon": [{"name": "Woven Charm", "bonus": "+5 HP"}],
    "Rare": [{"name": "Blade Totem", "bonus": "+5 ATK"}],
    "Heroic": [{"name": "Phantom Eye", "bonus": "+10 HP"}],
    "Epic": [{"name": "Dread Core", "bonus": "+10 ATK"}],
    "Legendary": [{"name": "Ember Sigil", "bonus": "+20 ATK / +20 HP"}]
}

def get_random_relic(player):
    floor = player.get("floor", 1)
    if floor >= 30:
        rarity = "Legendary"
    elif floor >= 25:
        rarity = "Epic"
    elif floor >= 20:
        rarity = "Heroic"
    elif floor >= 10:
        rarity = "Rare"
    elif floor >= 5:
        rarity = "Uncommon"
    else:
        rarity = "Common"

    relic = random.choice(RELIC_POOL[rarity])
    relic["rarity"] = rarity
    return relic

def apply_relic_effect(player, relic):
    if "+2 ATK" in relic["bonus"]:
        player
