import item as Item

def createItem():
    default_warrior_body = Item.Item()
    default_warrior_body.name = "Iron Armor"
    default_warrior_body.desc = "Default Warrior Stuff"
    default_warrior_body.slot = "body"
    default_warrior_body.armor = 3
    return default_warrior_body