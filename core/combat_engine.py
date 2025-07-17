import random

def resolve_pvp_duel(player1, player2):
    log = []
    p1_hp = player1["hp"]
    p2_hp = player2["hp"]
    p1_atk = player1["atk"]
    p2_atk = player2["atk"]

    turn = 1
    while p1_hp > 0 and p2_hp > 0:
        if turn % 2 == 1:
            p2_hp -= p1_atk
            log.append(f"{player1['name']} strikes for {p1_atk} damage! ({p2_hp} HP left)")
        else:
            p1_hp -= p2_atk
            log.append(f"{player2['name']} counters for {p2_atk} damage! ({p1_hp} HP left)")
        turn += 1

    if p1_hp <= 0 and p2_hp <= 0:
        result = "⚔️ It's a draw! Both fighters collapse."
    elif p1_hp <= 0:
        result = f"{player2['name']} wins the duel!"
    else:
        result = f"{player1['name']} wins the duel!"

    return result, log
