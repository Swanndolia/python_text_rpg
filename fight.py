from tools import clear_console as Tools

def fight(self, player, enemy, travel):
    Tools.clear_console()    
    if(player.health[0] <= 0):
        player_is_dead(player, enemy)
    elif(enemy.health <= 0):
        enemy_is_dead(player, enemy)
        travel(self, player)
    else:
        print(f"player.name : {player.health[0]} HP\n{enemy.name}: {enemy.health} HP")
        print(f"What you want to do {player.name} ? Attack (A), Spell (S), Item (I), Flee (F)")
        user_input = player.user_input()
        if user_input == "A":
            damage_calculation(player, enemy)
            fight(self, player, enemy, travel)
        elif user_input == "S":
            fight(self, player, enemy, travel)
        elif user_input == "I":
            fight(self, player, enemy, travel)
        elif user_input == "F":
            fight(self, player, enemy, travel)
        else:
            fight(self, player, enemy, travel)

def damage_calculation(player, enemy):
    if(player.stuff.rhand.two_hand):
        enemy.health -= player.stuff.rhand.damage + round(player.strength / 3)
    else:
        enemy.health -= player.stuff.rhand.damage + player.stuff.lhand.damage + player.strength
    if(enemy.strength > round(player.armor / 8)):
        player.health[0] -= enemy.strength - round(player.armor / 8)

def enemy_is_dead(player, enemy):
    print(f"{player.name} has killed {enemy.name}, you've won: {enemy.reward_gold} gold and {enemy.reward_exp} xp")
    player.gold += enemy.reward_gold
    player.exp += enemy.reward_exp
    if(player.exp >= player.next_lvl_exp):
        player.next_lvl_exp += round(player.next_lvl_exp * 1.1)
        player.unasigned_stats += 1
        player.lvl += 1
        print(f"Amazing ! you're now lvl {player.lvl}")
    player.mana[0] = player.mana[1]
    print("Press enter to return to menu")
    input()

def player_is_dead(player, enemy):
    print(f"{enemy.name} has killed {player.name}")
    print("Press enter to start a new game")
    input()
    Tools.clear_console()