import item as Item

def createItem():
    default_warrior_weapon = Item.Item()
    default_warrior_weapon.name = "Basic Sword"
    default_warrior_weapon.desc = "Default Warrior Stuff"
    default_warrior_weapon.slot = "rhand"
    default_warrior_weapon.damage = 1
    return default_warrior_weapon