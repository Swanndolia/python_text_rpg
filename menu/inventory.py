def inventory(self, player):
    print("This is your inventory:")
    for (i, item) in enumerate(player.inventory, start=1):
        print(i, item)
    print("This is your equiped stuff:")
    print(player.stuff)
    print("Press 0 to return to menu")
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)