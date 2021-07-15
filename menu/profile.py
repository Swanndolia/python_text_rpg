def profile(self, player):
    print(f"This is you:\n{player}Press 1 to set unnasigned stats points ({player.unasigned_stats})\n Else, press 0 to return to menu") 
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    elif (user_input == "1"):
        player.set_stats_points()
    else:
        profile(self, player)