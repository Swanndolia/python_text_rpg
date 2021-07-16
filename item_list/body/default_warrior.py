import item as Item

def createItem():
    default_warrior = Item.Item()
    default_warrior.name = "Iron Armor"
    default_warrior.desc = "Default Warrior Stuff"
    default_warrior.slot = "body"
    default_warrior.armor = 3
    return default_warrior