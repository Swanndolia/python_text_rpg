import enemy as Enemy

def create_enemy(lvl):
    bee = Enemy.Enemy()
    bee.lvl = lvl
    bee.health = 3 + round(lvl * 1.2)
    bee.strength = 3 + lvl
    bee.reward_exp = 5 + lvl
    bee.reward_gold = 3 + round(lvl / 3)
    bee.name = "Bee"
    bee.desc = " buzzzzzz"
    return bee