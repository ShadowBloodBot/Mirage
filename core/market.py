
import json
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

MARKET_FILE = "bot/data/market.json"
HISTORY_FILE = "bot/data/market_history.json"

def load_market():
    if not os.path.exists(MARKET_FILE):
        with open(MARKET_FILE, "w") as f:
            json.dump([], f)
    with open(MARKET_FILE, "r") as f:
        return json.load(f)

def save_market(data):
    with open(MARKET_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_history():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)
    with open(HISTORY_FILE, "r") as f:
        return json.load(f)

def save_history(data):
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def list_active_market():
    now = datetime.now(tz=ZoneInfo("Australia/Sydney"))
    return [item for item in load_market() if datetime.fromisoformat(item["expires"]) > now]

def post_market_item(seller_id, item_name, rarity, price, duration_hours):
    listings = load_market()
    now = datetime.now(tz=ZoneInfo("Australia/Sydney"))
    expiration = now + timedelta(hours=duration_hours)
    listings.append({
        "seller": str(seller_id),
        "item": item_name,
        "rarity": rarity,
        "price": price,
        "expires": expiration.isoformat()
    })
    save_market(listings)

def purchase_market_item(buyer_id, index):
    listings = load_market()
    item = listings.pop(index)
    save_market(listings)

    history = load_history()
    history.append({
        "buyer": str(buyer_id),
        "seller": item["seller"],
        "item": item["item"],
        "rarity": item["rarity"],
        "price": item["price"],
        "timestamp": datetime.now(tz=ZoneInfo("Australia/Sydney")).isoformat()
    })
    save_history(history)
    return item
