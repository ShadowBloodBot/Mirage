def create_profile(user) -> dict:
    return {
        "name": user.display_name,
        "hp": 100,
        "atk": 10,
        "gold": 0,
        "floor": 1,
        "relics": [],
        "inventory": [],
        "missions": [],
        "skilltree": [],
        "prestige": 0,
    }

def has_profile(user_id: str, data: dict) -> bool:
    return user_id in data.get("players", {})
