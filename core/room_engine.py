import random
from core.relic_system import get_random_relic, apply_relic_effect

def generate_room(player):
    floor = player["floor"]
    player["floor"] += 1

    rooms = [
        {
            "description": "You find a cracked statue radiating energy.",
            "actions": [{"label": "Touch It", "description": "Gain a random relic."}]
        },
        {
            "description": "A shadowy merchant offers you a gamble.",
            "actions": [{"label": "Gamble 10g", "description": "50% chance for a relic or loss."}]
        },
        {
            "description": "You hear whispers in the mist... a challenge awaits.",
            "actions": [{"label": "Enter Mist", "description": "Face a minor enemy."}]
        },
        {
            "description": "A healing spring bubbles here.",
            "actions": [{"label": "Rest", "description": "Recover 10 HP."}]
        }
    ]

    if floor % 5 == 0:
        return {
            "description": "🔥 A powerful force blocks your path... a boss approaches.",
            "actions": [{"label": "Prepare", "description": "Use `/mirage_boss` to engage the boss."}]
        }

    return random.choice(rooms)
