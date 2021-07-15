def shop(self, player):
    print("There's nothing here for now :/ come back later !")
    print("Press 0 to return to menu")
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    else:
        shop(self, player)