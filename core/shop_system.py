from core.relic_system import get_random_relic, apply_relic_effect
import random

def get_shop_inventory(player):
    return [
        {
            "name": "Mystic Charm",
            "description": "Gain +5 HP.",
            "cost": 20,
            "effect": lambda p: p.update({"hp": p["hp"] + 5})
        },
        {
            "name": "Warrior Stone",
            "description": "Gain +5 ATK.",
            "cost": 30,
            "effect": lambda p: p.update({"atk": p["atk"] + 5})
        },
        {
            "name": "Lucky Relic",
            "description": "Receive a random relic.",
            "cost": 40,
            "effect": lambda p: apply_relic_effect(p, get_random_relic(p))
        }
    ]

def buy_relic(player, item_name):
    shop_items = get_shop_inventory(player)
    for item in shop_items:
        if item["name"].lower() == item_name.lower():
            if player["gold"] < item["cost"]:
                return "❌ Not enough gold."
            item["effect"](player)
            player["gold"] -= item["cost"]
            return f"✅ You bought {item['name']}!"
    return "❌ Item not found."
