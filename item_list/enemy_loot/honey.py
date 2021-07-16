import item as Item

def createItem():
    honey = Item.Item()
    honey.name = "Honey"
    honey.desc = "Heal 20 HP"
    honey.slot = None
    honey.value = 10
    return honey