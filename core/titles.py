
import os, json

TITLES_FILE = "data/titles.json"
PLAYER_TITLES_DIR = "data/player_titles"

def ensure_dirs():
    if not os.path.exists(PLAYER_TITLES_DIR):
        os.makedirs(PLAYER_TITLES_DIR)

def get_player_titles_path(user_id):
    return f"{PLAYER_TITLES_DIR}/{user_id}.json"

def load_title_definitions():
    if not os.path.exists(TITLES_FILE):
        with open(TITLES_FILE, "w") as f:
            json.dump([
                {"id": "first_blood", "name": "First Blood", "rarity": "Bronze", "condition": "Win 1 duel"},
                {"id": "sanityless", "name": "The Insane", "rarity": "Silver", "condition": "Drop below 5 sanity"},
                {"id": "champion", "name": "Mirage Champion", "rarity": "Gold", "condition": "Reach level 25"},
                {"id": "godslayer", "name": "Godslayer", "rarity": "Mythic", "condition": "Defeat a world boss"},
            ], f, indent=2)
    with open(TITLES_FILE, "r") as f:
        return json.load(f)

def load_player_titles(user_id):
    ensure_dirs()
    path = get_player_titles_path(user_id)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({"equipped": None, "owned": []}, f)
    with open(path, "r") as f:
        return json.load(f)

def save_player_titles(user_id, data):
    path = get_player_titles_path(user_id)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def grant_title(user_id, title_id):
    titles = load_title_definitions()
    player_data = load_player_titles(user_id)
    if title_id not in player_data["owned"]:
        player_data["owned"].append(title_id)
    save_player_titles(user_id, player_data)

def equip_title(user_id, title_id):
    player_data = load_player_titles(user_id)
    if title_id in player_data["owned"]:
        player_data["equipped"] = title_id
        save_player_titles(user_id, player_data)
        return True
    return False

def get_equipped_title(user_id):
    player_data = load_player_titles(user_id)
    return player_data.get("equipped")

def get_title_by_id(title_id):
    for t in load_title_definitions():
        if t["id"] == title_id:
            return t
    return None
