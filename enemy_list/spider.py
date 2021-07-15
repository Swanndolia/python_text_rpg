import enemy as Enemy

def create_enemy(lvl):
    spider = Enemy.Enemy()
    spider.lvl = lvl
    spider.health = 6 + round(lvl * 1.3)
    spider.strength = 6 + round(lvl / 1.7)
    spider.reward_exp = 8 + lvl
    spider.reward_gold = 5 + round(lvl / 3)
    spider.name = "Spider"
    spider.desc = "I should avoid her bites"
    return spider