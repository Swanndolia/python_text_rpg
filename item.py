import tools as Tools


class Item():
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.value = 0
        self.damage = 0
        self.armor = 0
        self.slot = ""
        self.two_hand = False

    def __repr__(self):
        return Tools.printer.repr_item(self)
