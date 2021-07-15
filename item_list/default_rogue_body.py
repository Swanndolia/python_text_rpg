import item as Item

def createItem():
    default_rogue_body = Item.Item()
    default_rogue_body.name = "Leather Armor"
    default_rogue_body.desc = "Default Rogue Stuff"
    default_rogue_body.slot = "body"
    default_rogue_body.armor = 2
    return default_rogue_body