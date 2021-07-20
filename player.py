import pickle
import sys

import stuff as Stuff

import tools as Tools


class Player():
    def __init__(self):
        self.name = Tools.printer.whats_your_name()
        self.build = self.build_choice()
        self.lvl = 1
        self.exp = 0
        self.gold = 0
        self.unasigned_stats = 5
        self.next_lvl_exp = 100
        self.health = [50, 50]
        self.mana = [10, 10]
        self.agility = 0
        self.strength = 0
        self.dexterity = 0
        self.rapidity = 0
        self.luck = 0
        self.spells = []
        self.stuff = stuff
        self.inventory = []
        self.armor = self.calc_player_armor()

    def __repr__(self):
        return Tools.printer.repr_player(self)

    def user_input(self):
        try:
            user_input = input(">>> ").upper()
            return user_input
        except KeyboardInterrupt:
            self.save_progress()
            sys.exit(1)

    def build_choice(self):
        Tools.clear_console()
        Tools.printer.build_choice(self)
        user_input = self.user_input()
        if user_input == "1":
            stuff.set_mage_stuff()
            return "Mage"
        elif user_input == "2":
            stuff.set_warrior_stuff()
            return "Warrior"
        elif user_input == "3":
            stuff.set_rogue_stuff()
            return "Rogue"
        elif user_input == "4":
            stuff.set_aquero_stuff()
            return "Aquero"
        else:
            self.build_choice()

    def add_item_to_inventory(self, item):
        player.inventory.append(item)

    def calc_player_armor(self):
        return self.stuff.body.armor + self.stuff.boots.armor + self.stuff.head.armor + self.stuff.legs.armor + self.stuff.lhand.armor

    def equip_item(self, item):
        if(item.slot == "head"):
            if(stuff.head.name != ""):
                self.inventory.append(stuff.head)
            stuff.head = item

        elif(item.slot == "body"):
            if(stuff.body.name != ""):
                self.inventory.append(stuff.body)
            stuff.body = item

        elif(item.slot == "legs"):
            if(stuff.legs.name != ""):
                self.inventory.append(stuff.legs)
            stuff.legs = item

        elif(item.slot == "boots"):
            if(stuff.boots.name != ""):
                self.inventory.append(stuff.boots)
            stuff.boots = item

        elif(item.slot == "rhand"):
            if(stuff.rhand.name != ""):
                self.inventory.append(stuff.rhand)
            stuff.rhand = item

        elif(item.slot == "lhand"):
            if(stuff.lhand.name != ""):
                self.inventory.append(stuff.lhand)
            stuff.lhand = item

        elif(item.slot == "anyhand"):
            # TODO
            return

    def set_stats_points(self):

        if(self.unasigned_stats != 0):
            Tools.clear_console()
            Tools.printer.assign_stats(self)
            user_input = self.user_input()
            if(user_input == "1"):
                self.health[1] += 10
                self.unasigned_stats -= 1
            elif(user_input == "2"):
                self.mana[1] += 10
                self.unasigned_stats -= 1
            elif(user_input == "3"):
                self.agility += 1
                self.unasigned_stats -= 1
            elif(user_input == "4"):
                self.strength += 1
                self.unasigned_stats -= 1
            elif(user_input == "5"):
                self.rapidity += 1
                self.unasigned_stats -= 1
            elif(user_input == "6"):
                self.dexterity += 1
                self.unasigned_stats -= 1
            elif(user_input == "7"):
                self.luck += 1
                self.unasigned_stats -= 1
            elif(user_input == "0"):
                return
            self.set_stats_points()
        else:
            Tools.clear_console()
            Tools.printer.assign_stats(self)
            self.user_input()
            return

    def save_progress(self):
        save_file = open('player_save_file.obj', 'wb')
        pickle.dump(self, save_file)
        save_file.close()


Tools.clear_console()

stuff = Stuff.Stuff()

try:
    save_file = open('player_save_file.obj', 'rb')
    Tools.printer.save_found()
    load_or_no = input().upper()
    if(load_or_no == "1"):
        player = pickle.load(save_file)
        save_file.close()
    else:
        save_file.close()
        player = Player()
except FileNotFoundError:
    player = Player()
