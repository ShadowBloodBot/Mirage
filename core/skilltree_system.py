def get_skill_tree(player):
    # Static skill tree example
    tree = [
        {"id": "s1", "name": "Sharp Instinct", "description": "+5% crit chance", "unlocked": "s1" in player["skilltree"]},
        {"id": "s2", "name": "Enduring Soul", "description": "+10 max HP", "unlocked": "s2" in player["skilltree"]},
        {"id": "s3", "name": "Greedy Grip", "description": "+25% gold drops", "unlocked": "s3" in player["skilltree"]}
    ]
    return tree

def unlock_skill(player, skill_id):
    if skill_id in player["skilltree"]:
        return "❌ Skill already unlocked."
    player["skilltree"].append(skill_id)
    return f"✅ Unlocked skill {skill_id}!"
