import item as Item

def createItem():
    default_mage = Item.Item()
    default_mage.name = "Basic Staff"
    default_mage.desc = "Default Mage Stuff"
    default_mage.slot = "rhand"
    default_mage.damage = 5
    default_mage.two_hand = True
    return default_mage