def shop(self, player):
    print(f"There's nothing here for now :/ come back later !")
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    else:
        shop(self, player)