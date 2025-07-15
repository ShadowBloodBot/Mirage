def get_active_missions(player):
    # Static example missions
    return [
        {"id": "m1", "title": "First Blood", "description": "Win your first duel."},
        {"id": "m2", "title": "Treasure Hunter", "description": "Loot a relic."},
        {"id": "m3", "title": "Onward!", "description": "Reach floor 10."}
    ]

def complete_missions(player):
    completed = []
    floor = player.get("floor", 1)
    relics = player.get("relics", [])
    missions = get_active_missions(player)

    for m in missions:
        if m["id"] == "m1" and player.get("duel_wins", 0) >= 1:
            completed.append("m1")
        if m["id"] == "m2" and len(relics) > 0:
            completed.append("m2")
        if m["id"] == "m3" and floor >= 10:
            completed.append("m3")

    player["missions"] = completed
    return completed
