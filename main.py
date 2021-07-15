import player as Player
import enemy as Enemy

import menu

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
        print(f"What do you want to do {player.name} ?\nTravel (T), Inventory (I), Skills (S), Profile (P)")
        user_input = player.user_input()
        Tools.clear_console()
        if user_input == "T":
            menu.travel(self, player)
        elif user_input == "I":
            menu.inventory(self, player)
        elif user_input == "S":
            menu.skills(self, player)
        elif user_input == "P":
            menu.profile(self, player)
        else:
            self.menu_choice(player)
        return

game = Game()

game.main_loop(Player.player)