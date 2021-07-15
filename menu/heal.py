def heal(self, player):
    cost = round(1+ (player.health[1] - player.health[0]) / 10)
    print(f"Hello {player.name}, you currently have {player.health[0]} HP\nPress 1 to heal all your hp ({player.health[0]} / {player.health[1]} it will cost you {cost} gold. Else, press 0 to return to menu")
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    elif (user_input == "1"):
        if(player.gold >= cost):
            player.health[0] = player.health[1]
            player.gold -= cost
            print("You've been successfully healed ! Press enter to continue")
        else:
            print(f"You dont have enough gold ({player.gold} / {cost}) ! Press enter to continue")
        input()
    else:
        heal(self, player)
