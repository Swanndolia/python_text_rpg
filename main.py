import player as Player
import enemy as Enemy

import menus

from tools import clear_console as Tools

class Game():
    def __init__(self):
        self.name = "GAME"

    def main_loop(self, player):
        while (player.health[0] > 0):
            self.menu_choice(player)
        player = Player.Player()
        self.main_loop(player)

    def menu_choice(self, player):
        Tools.clear_console()
        print("What do you want to do " + player.name +
            " ? : Travel (T), Inventory (I), Skills (S), Profile (P)")
        user_input = player.user_input()
        Tools.clear_console()
        if user_input == "T":
            menus.menu_travel(self, player)
        elif user_input == "I":
            menus.menu_inventory(self, player)
        elif user_input == "S":
            menus.menu_skills(self, player)
        elif user_input == "P":
            menus.menu_profile(self, player)
        else:
            self.menu_choice(player)
        return

game = Game()

game.main_loop(Player.player)