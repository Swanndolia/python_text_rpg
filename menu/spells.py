def spells(self, player):
    print(f"This is the list of your spells: {player.spells}")
    print("Press 0 to return to menu")
    if(player.user_input() == "0"):
        self.menu_choice(player)