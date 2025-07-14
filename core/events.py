
import os, json, random, datetime

EVENTS_FILE = "data/global_event.json"
EVENT_POOL = [
    {"id": "storm_challenge", "name": "Lightning Trial", "effect": "⚡ All battles deal 25% more damage", "type": "buff"},
    {"id": "fog_madness", "name": "Mist of Confusion", "effect": "🌀 Sanity drains 2x faster", "type": "debuff"},
    {"id": "merchant_blessing", "name": "Golden Merchant", "effect": "💰 Shop prices reduced 20%", "type": "buff"},
    {"id": "phantom_twist", "name": "Phantom Encounters", "effect": "👻 Rooms spawn 2x enemies", "type": "chaos"},
    {"id": "blood_moon", "name": "Blood Moon", "effect": "🌕 Rare enemies become more common", "type": "chaos"},
]

ROTATION_INTERVAL_HOURS = 24

def get_current_event():
    if not os.path.exists(EVENTS_FILE):
        rotate_event()
    with open(EVENTS_FILE, "r") as f:
        data = json.load(f)
        return data

def rotate_event(force=False):
    if not os.path.exists(EVENTS_FILE) or force:
        event = random.choice(EVENT_POOL)
        data = {
            "event": event,
            "start_time": datetime.datetime.utcnow().isoformat()
        }
        with open(EVENTS_FILE, "w") as f:
            json.dump(data, f, indent=2)
        return event

    with open(EVENTS_FILE, "r") as f:
        data = json.load(f)
        last = datetime.datetime.fromisoformat(data["start_time"])
        now = datetime.datetime.utcnow()
        if (now - last).total_seconds() > ROTATION_INTERVAL_HOURS * 3600:
            return rotate_event(force=True)
        return data["event"]
