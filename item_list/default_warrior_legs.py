import item as Item

def createItem():
    default_warrior_legs = Item.Item()
    default_warrior_legs.name = "Iron Leggings"
    default_warrior_legs.desc = "Default Warrior Stuff"
    default_warrior_legs.slot = "legs"
    default_warrior_legs.armor = 3
    return default_warrior_legs