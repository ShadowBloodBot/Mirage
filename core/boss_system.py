def generate_boss_encounter(player):
    floor = player.get("floor", 1)
    if floor <= 5:
        return {
            "name": "Stone Golem",
            "description": "A lumbering guardian of the ancient halls.",
            "moves": [
                {"name": "Slam", "effect": "Deals 15 damage."},
                {"name": "Roar", "effect": "Lowers your ATK by 2 temporarily."}
            ]
        }
    elif floor <= 10:
        return {
            "name": "Wraith Matron",
            "description": "A ghostly terror that feeds on fear.",
            "moves": [
                {"name": "Haunt", "effect": "Deals 20 damage and heals 10 HP."},
                {"name": "Fade", "effect": "Dodges next attack."}
            ]
        }
    else:
        return {
            "name": "Ember Lord",
            "description": "Born from flame, he incinerates the unworthy.",
            "moves": [
                {"name": "Inferno", "effect": "Deals 30 damage."},
                {"name": "Ember Shield", "effect": "Reduces damage by half for 2 turns."}
            ]
        }
