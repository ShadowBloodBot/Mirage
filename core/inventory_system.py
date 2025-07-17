def add_item(player, item_name):
    if "inventory" not in player:
        player["inventory"] = []
    player["inventory"].append(item_name)

def use_item(player, item_name):
    if item_name not in player["inventory"]:
        return "❌ Item not found in inventory."
    
    if item_name.lower() == "healing potion":
        player["hp"] += 20
        player["inventory"].remove(item_name)
        return "🧪 You used a Healing Potion and restored 20 HP!"
    
    return "❓ That item has no effect."

def discard_item(player, item_name):
    if item_name in player["inventory"]:
        player["inventory"].remove(item_name)
        return f"🗑️ You discarded {item_name}."
    return "❌ Item not found."
