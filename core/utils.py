import json
import os
from datetime import datetime
import dropbox

DB_FILE = "db.json"

def load_data() -> dict:
    if not os.path.exists(DB_FILE):
        return {"players": {}}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_data(data: dict):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def format_relic(relic: dict) -> str:
    bonus = relic.get("bonus", "")
    rarity = relic.get("rarity", "Common")
    return f"({rarity}) {bonus}"

def create_dropbox_backup() -> str:
    token = os.getenv("DROPBOX_TOKEN")
    if not token:
        return "No token found"

    dbx = dropbox.Dropbox(token)
    with open(DB_FILE, "rb") as f:
        content = f.read()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        path = f"/mirage_backups/db_{timestamp}.json"
        dbx.files_upload(content, path)
        return path
