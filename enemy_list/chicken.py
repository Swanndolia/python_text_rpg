import enemy as Enemy

def create_enemy(lvl):
    chicken = Enemy.Enemy()
    chicken.lvl = lvl
    chicken.health = 10 + lvl * 2
    chicken.strength = 2 + round(lvl / 3)
    chicken.reward_exp = 5 + lvl
    chicken.reward_gold = 3 + round(lvl / 3)
    chicken.name = "Chicken"
    chicken.desc = "it have a lot of feather"
    return chicken