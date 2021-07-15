def fight(player, enemy):
    if(player.health == 0):
        print(enemy.name + " has killed " + player.name)
        print("Press enter to return to menu")
        input()
        return
    elif(enemy.health == 0):
        print(player.name + " has killed " + enemy.name + ", you've won: " +
              str(enemy.reward_gold) + " gold and " + str(enemy.reward_exp) + " xp")
        player.gold += enemy.reward_gold
        player.exp += enemy.reward_exp
        print("Press enter to return to menu")
        input()
        return
    else:
        print(player.name + ": " + str(player.health) +
              " " + enemy.name + ": " + str(enemy.health))
        print("What you want to do " + player.name +
              " Attack (A), Spell (S), Item (I), Flee (F)")
        user_input = player.user_input()
        if user_input == "A":
            enemy.health -= player.stuff.rhand.damage + player.strength
            player.health -= enemy.strength
            fight(player, enemy)
        elif user_input == "S":
            fight(player, enemy)
        elif user_input == "I":
            fight(player, enemy)
        elif user_input == "F":
            fight(player, enemy)
        else:
            fight(player, enemy)
