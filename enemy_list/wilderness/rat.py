import enemy as Enemy

def create_enemy(lvl):
    rat = Enemy.Enemy()
    rat.lvl = lvl
    rat.health = 7 + round(lvl * 1.5)
    rat.strength = 3 + round(lvl / 2)
    rat.reward_exp = 5 + lvl 
    rat.reward_gold = 3 + round(lvl / 3)
    rat.name = "Rat"
    rat.desc = "it smell !"
    return rat