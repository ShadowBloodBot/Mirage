
import random, json, os
from datetime import datetime, timedelta
from bot.core.profile import get_profile_path

DAILY_MISSIONS = [
    {"type": "clear", "goal": 3, "reward": 75},
    {"type": "duel_win", "goal": 1, "reward": 100},
    {"type": "gold_gain", "goal": 200, "reward": 60},
    {"type": "item_find", "goal": 1, "reward": 90},
    {"type": "sanity_spent", "goal": 100, "reward": 70},
]

WEEKLY_MISSIONS = [
    {"type": "elite_kill", "goal": 2, "reward": 250},
    {"type": "total_rooms", "goal": 20, "reward": 180},
    {"type": "shop_buys", "goal": 5, "reward": 150},
    {"type": "gold_spent", "goal": 500, "reward": 200},
    {"type": "relic_use", "goal": 5, "reward": 170},
]

def generate_missions():
    return {
        "daily": random.sample(DAILY_MISSIONS, 3),
        "weekly": random.sample(WEEKLY_MISSIONS, 2),
        "last_reset": datetime.now().isoformat(),
        "progress": {}
    }

def get_missions_path(user_id):
    return f"data/missions/{user_id}.json"

def load_or_generate_missions(user_id):
    path = get_missions_path(user_id)
    if not os.path.exists("data/missions"):
        os.makedirs("data/missions", exist_ok=True)

    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
        last_reset = datetime.fromisoformat(data.get("last_reset", "2000-01-01"))
        now = datetime.now()
        if now - last_reset > timedelta(days=1):
            data = generate_missions()
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
    else:
        data = generate_missions()
        with open(path, "w") as f:
            json.dump(data, f, indent=2)

    return data

def update_mission_progress(user_id, mtype, amount=1):
    path = get_missions_path(user_id)
    data = load_or_generate_missions(user_id)
    data["progress"][mtype] = data["progress"].get(mtype, 0) + amount
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def claim_reward(user_id, category, index):
    path = get_missions_path(user_id)
    data = load_or_generate_missions(user_id)
    mission_list = data.get(category, [])
    if index >= len(mission_list):
        return None
    mission = mission_list[index]
    key = f"{category}_{index}_claimed"
    if data.get(key):
        return None
    if data["progress"].get(mission["type"], 0) >= mission["goal"]:
        data[key] = True
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return mission["reward"]
    return None
