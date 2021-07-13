def menu_profile(self, player):
    print(player)
    print("Press 0 to return to menu")
    if(player.user_input() == "0"):
        self.menu_choice(player)