def skills(self, player):
    print("This is the list of your skills:")
    print(player.skills)
    print("Press 0 to return to menu")
    if(player.user_input() == "0"):
        self.menu_choice(player)