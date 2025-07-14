
import os, json

GUILD_DIR = "data/guilds"

def get_guild_path(guild_id):
    return f"{GUILD_DIR}/{guild_id}.json"

def ensure_guilds_dir():
    if not os.path.exists(GUILD_DIR):
        os.makedirs(GUILD_DIR)

def create_guild(user_id, name, emoji, description):
    ensure_guilds_dir()
    guild_id = str(user_id)  # using creator's ID as initial guild ID
    path = get_guild_path(guild_id)
    if os.path.exists(path):
        return None  # already created

    data = {
        "id": guild_id,
        "name": name,
        "emoji": emoji,
        "description": description,
        "leader": user_id,
        "officers": [],
        "members": [user_id],
        "vault": {"gold": 0, "items": []},
        "perks": {}
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    return data

def load_guild(guild_id):
    path = get_guild_path(guild_id)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None

def save_guild(data):
    path = get_guild_path(data["id"])
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def find_user_guild(user_id):
    ensure_guilds_dir()
    for filename in os.listdir(GUILD_DIR):
        path = os.path.join(GUILD_DIR, filename)
        with open(path, "r") as f:
            data = json.load(f)
            if user_id in data.get("members", []):
                return data
    return None

def leave_guild(user_id):
    guild = find_user_guild(user_id)
    if not guild:
        return False
    if guild["leader"] == user_id:
        return False  # leader must disband
    if user_id in guild["members"]:
        guild["members"].remove(user_id)
        if user_id in guild["officers"]:
            guild["officers"].remove(user_id)
        save_guild(guild)
        return True
    return False
