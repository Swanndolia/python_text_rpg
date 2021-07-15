import item as Item

def createItem():
    default_mage_weapon = Item.Item()
    default_mage_weapon.name = "Basic Staff"
    default_mage_weapon.desc = "Default Mage Stuff"
    default_mage_weapon.slot = "rhand"
    default_mage_weapon.damage = 5
    default_mage_weapon.two_hand = True
    return default_mage_weapon