import item as Item

def createItem():
    default_mage_body = Item.Item()
    default_mage_body.name = "Cloth Tunic"
    default_mage_body.desc = "Default Mage Stuff"
    default_mage_body.slot = "body"
    default_mage_body.armor = 2
    return default_mage_body