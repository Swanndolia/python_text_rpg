import item as Item

def createItem():
    default_warrior = Item.Item()
    default_warrior.name = "Basic Sword"
    default_warrior.desc = "Default Warrior Stuff"
    default_warrior.slot = "rhand"
    default_warrior.damage = 1
    return default_warrior