import enemy as Enemy

def create_enemy(lvl):
    wolf = Enemy.Enemy()
    wolf.lvl = lvl
    wolf.health = 10 + lvl * 2
    wolf.strength = 4 + round(lvl / 2)
    wolf.reward_exp = 8 + lvl
    wolf.reward_gold = 5 + round(lvl / 3)
    wolf.name = "Wolf"
    wolf.desc = "it seems really dangerous"
    return wolf 