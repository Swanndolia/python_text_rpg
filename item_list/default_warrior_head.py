import item as Item

def createItem():
    default_warrior_head = Item.Item()
    default_warrior_head.name = "Iron Helmet"
    default_warrior_head.desc = "Default Warrior Stuff"
    default_warrior_head.slot = "head"
    default_warrior_head.armor = 3
    return default_warrior_head