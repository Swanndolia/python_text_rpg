import item as Item
import item_list

class Stuff():
    def __init__(self):
        self.head = head
        self.body = body
        self.legs = legs
        self.boots = boots
        self.rhand = rhand
        self.lhand = lhand

    def __repr__(self):
        return f"\nHead: {self.head}\nBody: {self.body}\nLlegs: {self.legs}\nBoots: {self.boots}\nLeft Hand: {self.lhand}\nRight Hand: {self.rhand}\n"
    
    def set_warrior_stuff(self):
        self.head = item_list.default_warrior_body.createItem()
        self.body = item_list.default_warrior_body.createItem()
        self.legs = item_list.default_warrior_legs.createItem()
        self.boots = item_list.default_warrior_boots.createItem()
        self.rhand = item_list.default_warrior_weapon.createItem()
        self.lhand = item_list.default_warrior_shield.createItem()


    def set_aquero_stuff(self):
        self.head = item_list.default_aquero_head.createItem()
        self.body = item_list.default_aquero_body.createItem()
        self.legs = item_list.default_aquero_legs.createItem()
        self.boots = item_list.default_aquero_boots.createItem()
        self.rhand = item_list.default_aquero_weapon.createItem()
        if(self.rhand.two_hand):
            self.lhand = self.rhand
    
    def set_rogue_stuff(self):
        self.head = item_list.default_rogue_head.createItem()
        self.body = item_list.default_rogue_body.createItem()
        self.legs = item_list.default_rogue_legs.createItem()
        self.boots = item_list.default_rogue_boots.createItem()
        self.rhand = item_list.default_rogue_weapon.createItem()
        self.lhand = item_list.default_rogue_weapon.createItem()
        if(self.rhand.two_hand):
            self.lhand = self.rhand

    def set_mage_stuff(self):
        self.head = item_list.default_mage_head.createItem()
        self.body = item_list.default_mage_body.createItem()
        self.legs = item_list.default_mage_legs.createItem()
        self.boots = item_list.default_mage_boots.createItem()
        self.rhand = item_list.default_mage_weapon.createItem()
        if(self.rhand.two_hand):
            self.lhand = self.rhand


head = Item.Item()
body = Item.Item()
legs = Item.Item()
boots = Item.Item()
lhand = Item.Item()
rhand = Item.Item()
