import enemy as Enemy
import item_list.enemy_loot

honey_10 = [100, item_list.enemy_loot.honey.createItem()]

def create_enemy(lvl):
    bee = Enemy.Enemy()
    bee.lvl = lvl
    bee.health = 3 + round(lvl * 1.2)
    bee.strength = 3 + lvl
    bee.reward_exp = 5 + lvl
    bee.reward_gold = 3 + round(lvl / 3)
    bee.name = "Bee"
    bee.desc = " buzzzzzz"
    bee.loot.append(honey_10)
    return bee