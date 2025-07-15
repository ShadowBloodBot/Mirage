def can_prestige(player):
    return player.get("floor", 0) >= 50

def perform_prestige(player):
    bonus = f"+1 permanent ATK per prestige level ({player['prestige'] + 1})"
    player["prestige"] += 1
    player["atk"] += 1
    player["floor"] = 1
    player["hp"] = 100
    player["gold"] = 0
    player["relics"] = []
    player["inventory"] = []
    player["missions"] = []
    return bonus
