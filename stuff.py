import item as Item
import item_list
import tools as Tools

class Stuff():
    def __init__(self):
        self.head = head
        self.body = body
        self.legs = legs
        self.boots = boots
        self.rhand = rhand
        self.lhand = lhand

    def __repr__(self):
        return Tools.printer.repr_stuff(self)
    
    def set_warrior_stuff(self):
        self.head = item_list.head.default_warrior.createItem()
        self.body = item_list.body.default_warrior.createItem()
        self.legs = item_list.legs.default_warrior.createItem()
        self.boots = item_list.boots.default_warrior.createItem()
        self.rhand = item_list.weapon.default_warrior.createItem()
        self.lhand = item_list.shield.default_warrior.createItem()


    def set_aquero_stuff(self):
        self.head = item_list.head.default_aquero.createItem()
        self.body = item_list.body.default_aquero.createItem()
        self.legs = item_list.legs.default_aquero.createItem()
        self.boots = item_list.boots.default_aquero.createItem()
        self.rhand = item_list.weapon.default_aquero.createItem()
        if(self.rhand.two_hand):
            self.lhand = self.rhand
    
    def set_rogue_stuff(self):
        self.head = item_list.head.default_rogue.createItem()
        self.body = item_list.body.default_rogue.createItem()
        self.legs = item_list.legs.default_rogue.createItem()
        self.boots = item_list.boots.default_rogue.createItem()
        self.rhand = item_list.weapon.default_rogue.createItem()
        self.lhand = item_list.weapon.default_rogue.createItem()
        if(self.rhand.two_hand):
            self.lhand = self.rhand

    def set_mage_stuff(self):
        self.head = item_list.head.default_mage.createItem()
        self.body = item_list.body.default_mage.createItem()
        self.legs = item_list.legs.default_mage.createItem()
        self.boots = item_list.boots.default_mage.createItem()
        self.rhand = item_list.weapon.default_mage.createItem()
        if(self.rhand.two_hand):
            self.lhand = self.rhand


head = Item.Item()
body = Item.Item()
legs = Item.Item()
boots = Item.Item()
lhand = Item.Item()
rhand = Item.Item()
