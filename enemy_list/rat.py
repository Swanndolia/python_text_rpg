import enemy as Enemy

def create_enemy(lvl):
    rat = Enemy.Enemy()
    rat.lvl = lvl
    rat.health = 7 + lvl * 2
    rat.strength = 3 + lvl
    rat.reward_exp = 5
    rat.reward_gold = 3
    rat.name = "Rat"
    rat.desc = "it smell !"
    return rat