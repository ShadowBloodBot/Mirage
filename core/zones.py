
ZONES = [
    {
        "id": "whispers_woods",
        "name": "🌲 Whispers Woods",
        "unlocks_at": 0,
        "description": "The trees whisper secrets from forgotten times. Sanity fades slower here.",
        "enemy_scaling": 1.0,
        "sanity_drain": 0.8,
        "relic_bonus": ["Calmroot", "Barkskin"]
    },
    {
        "id": "howling_ruins",
        "name": "🏛️ Howling Ruins",
        "unlocks_at": 20,
        "description": "Ancient echoes twist your mind. Stronger foes dwell within.",
        "enemy_scaling": 1.5,
        "sanity_drain": 1.2,
        "relic_bonus": ["Howlstone", "Shatter Glyph"]
    },
    {
        "id": "the_sunken_hall",
        "name": "🌊 The Sunken Hall",
        "unlocks_at": 40,
        "description": "Once a temple, now submerged. Sanity loss accelerates — but so do the rewards.",
        "enemy_scaling": 2.0,
        "sanity_drain": 1.6,
        "relic_bonus": ["Tideborn Mask", "Echo Pearl"]
    }
]

def get_unlocked_zones(clears):
    return [zone for zone in ZONES if clears >= zone["unlocks_at"]]

def get_zone_by_id(zone_id):
    for zone in ZONES:
        if zone["id"] == zone_id:
            return zone
    return ZONES[0]

def get_zone_names():
    return [zone["name"] for zone in ZONES]

def get_default_zone():
    return ZONES[0]["id"]
