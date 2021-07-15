def heal(self, player):
    print("Hello " + player.name + ", you currently have " +
          str(player.health[0]) + " HP")
    cost = round(1+ (player.health[1] - player.health[0]) / 10)
    print("Press 1 to heal all your hp (" + str(player.health[0]) + " / " + str(
        player.health[1]) + ") it will cost you " + str(cost))
    print("Press 0 to return to menu")
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    elif (user_input == "1"):
        if(player.gold >= cost):
            player.health[0] = player.health[1]
            player.gold -= cost
            print("You've been successfully healed ! Press enter to continue")
        else:
            print("You dont have enough gold (" +
                  str(player.gold) + "/" + str(cost) + ") ! Press enter to continue")
        input()
    else:
        heal(self, player)
