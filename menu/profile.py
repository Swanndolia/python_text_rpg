def profile(self, player):
    print("This is you:")
    print(player)
    print("Press 1 to set unnasigned stats points (" + str(player.unasigned_stats) + ")" )
    print("Press 0 to return to menu")
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    elif (user_input == "1"):
        player.set_stats_points()
    else:
        profile(self, player)