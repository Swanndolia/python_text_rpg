def menu_inventory(self, player):
    print(player.inventory)
    print(player.stuff)
    print("Press 0 to return to menu")
    if(player.user_input() == "0"):
        self.menu_choice(player)