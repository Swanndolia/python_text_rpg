import tools as Tools

class Spells():
    def __init__(self):
        self.id = 0
        self.name = ""
        self.desc = ""
        self.damage = 0
        self.mp_cost = 0

    def __repr__(self):
        return Tools.printer.repr_spells(self)