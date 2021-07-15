def skills(self, player):
    print(f"This is the list of your skills: {player.skills}")
    print("Press 0 to return to menu")
    if(player.user_input() == "0"):
        self.menu_choice(player)