class Spells():
    def __init__(self):
        self.id = 0
        self.name = ""
        self.desc = ""
        self.damage = 0
        self.mp_cost = 0

    def __repr__(self):
        return f"\nid: {self.id}\nname: {self.name}\ndesc: {self.desc}\ndamage: {self.damage}\nmp cost: {self.mp_cost}\n"