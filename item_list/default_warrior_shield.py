import item as Item

def createItem():
    default_warrior_shield = Item.Item()
    default_warrior_shield.name = "Basic Shield"
    default_warrior_shield.desc = "Default Warrior Stuff"
    default_warrior_shield.slot = "lhand"
    default_warrior_shield.armor = 3
    return default_warrior_shield