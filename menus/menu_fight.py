def menu_fight(self, player):
    print("Press 0 to return to menu")
    user_input = player.user_input()
    
    if(user_input == "0"):
        self.menu_choice(player)
