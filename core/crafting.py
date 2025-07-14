
import os, json, random

CRAFTING_RECIPES_FILE = "data/recipes.json"
PLAYER_INVENTORY_DIR = "data/inventories"

def ensure_dirs():
    if not os.path.exists(PLAYER_INVENTORY_DIR):
        os.makedirs(PLAYER_INVENTORY_DIR)

def get_inventory_path(user_id):
    return f"{PLAYER_INVENTORY_DIR}/{user_id}.json"

def load_inventory(user_id):
    ensure_dirs()
    path = get_inventory_path(user_id)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({"items": []}, f)
    with open(path, "r") as f:
        return json.load(f)

def save_inventory(user_id, data):
    path = get_inventory_path(user_id)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def add_item_to_inventory(user_id, item_name, rarity):
    data = load_inventory(user_id)
    data["items"].append({"name": item_name, "rarity": rarity})
    save_inventory(user_id, data)

def remove_items(user_id, item_names):
    data = load_inventory(user_id)
    data["items"] = [i for i in data["items"] if i["name"] not in item_names]
    save_inventory(user_id, data)

def load_recipes():
    if not os.path.exists(CRAFTING_RECIPES_FILE):
        with open(CRAFTING_RECIPES_FILE, "w") as f:
            json.dump([
                {"inputs": ["Iron Shard", "Flame Core"], "output": {"name": "Blazing Blade", "rarity": "Rare"}},
                {"inputs": ["Crystal Wing", "Dark Essence"], "output": {"name": "Wraith Cloak", "rarity": "Epic"}}
            ], f, indent=2)
    with open(CRAFTING_RECIPES_FILE, "r") as f:
        return json.load(f)

def try_craft(user_id, item_names):
    recipes = load_recipes()
    inv = load_inventory(user_id)
    inv_names = [i["name"] for i in inv["items"]]

    for recipe in recipes:
        if sorted(recipe["inputs"]) == sorted(item_names):
            # check all inputs exist
            if all(name in inv_names for name in item_names):
                remove_items(user_id, item_names)
                add_item_to_inventory(user_id, recipe["output"]["name"], recipe["output"]["rarity"])
                return recipe["output"]
    return None

def random_fusion(user_id):
    inv = load_inventory(user_id)
    if len(inv["items"]) < 2:
        return None, "Need at least 2 items to fuse."

    fused_name = f"Fused Relic #{random.randint(1000,9999)}"
    rarity = random.choices(["Common", "Uncommon", "Rare", "Epic"], weights=[50, 30, 15, 5])[0]
    chosen_items = random.sample(inv["items"], 2)
    for i in chosen_items:
        inv["items"].remove(i)
    inv["items"].append({"name": fused_name, "rarity": rarity})
    save_inventory(user_id, inv)
    return {"name": fused_name, "rarity": rarity}, None
