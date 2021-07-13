def menu_fight(self, player):
    print("fight")
    print("Press 0 to return to menu")
    if(player.user_input() == "0"):
        self.menu_choice(player)
