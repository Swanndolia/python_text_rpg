import item as Item

def createItem():
    default_warrior_boots = Item.Item()
    default_warrior_boots.name = "Iron Boots"
    default_warrior_boots.desc = "Default Warrior Stuff"
    default_warrior_boots.slot = "boots"
    default_warrior_boots.armor = 3
    return default_warrior_boots