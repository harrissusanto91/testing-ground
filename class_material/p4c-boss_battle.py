# ASCII Art for Player and Boss  
player_art = r"""  
       O  
      /|\
      / \
"""  

idle_boss_art = r"""  
                     ,     /\     ,  
                    / |   (  )   | \
                   /__|_   \/   _|__\
                    (O)   /\   (O)  
                   __/|\__/__\__/|\__  
                  _,-'    ,    ___    ,       '-._  
                _,-'      \  /,-'   `-./ \         '-.   
             |        |    / (    .-.    )  |         |   
              \       \   /   '-.(o_o).-'   /           \  
               `.       '-.   '-'   .-'              `.   
                 '-.___.-'                   -->         |  
                 |                                             |  
                 \                _.-'                     /  
                  '-._                             _.-'  
                      '--._                     _.-'  
                           '--._____.--'  
"""  

attack_boss_art = r"""  
                     ,     /\     ,  
                    / |   (  )   | \
                   /__|_   \/   _|__\
                    (O)   /\   (O)  
                   __/|\__/__\__/|\__  
                     _,-'      \  /.-'   `-./ \         '-.  
             |        |    / (   O   O    )  |         |   
              \       \   /   '-.  /-\ .-'   /           \  
               `.       '-.   '-'   .-'              `.   
                 '-.___.-'                   -->         |  
                  |       *##*                              |  
                 |    :%%%%%:                               |  
                 |   =%%%%%%%%#                             |  
                 |   +%%%%%%%+                             |  
                 |    =*#####*=                         |  
                   ----.____             ______   _.-'  
                           '--._____.--'  
"""  

# Boss attributes  
boss_name = "The Demon Lord"  
boss_health = 150  
boss_attack_damage = 20  # Fixed damage the boss does  
strong_attack_damage = 40  # Boss strong attack damage  

# Player attributes  
player_health = 100  
player_attack_damage = 30  # Fixed damage the player does  
defense_multiplier = 0.5  # Defend reduces damage taken by half  

# Start with the boss in idle mode  
boss_mode = "idle"  

while player_health > 0 and boss_health > 0:  
    # Display the current battle scene based on the boss mode  
    if boss_mode == "idle":  
        print(idle_boss_art)  
    elif boss_mode == "attack":  
        print(attack_boss_art)  
    print(player_art)  

    # Display health status  
    print(f"\nYour Health: {player_health}")  
    print(f"{boss_name}'s Health: {boss_health}")  

    # Player's turn  
    action = input("\nChoose your action: (1) Attack (2) Defend: ")  

    if boss_mode == "idle":  
        if action == "1":  
            # Player attacks boss  
            boss_health -= player_attack_damage  
            print(f"You attack {boss_name} for {player_attack_damage} damage!")  
            # Change boss mode to attack after player's attack  
            boss_mode = "attack"  
        elif action == "2":  
            print("You brace yourself for the incoming attack, but nothing happens this turn.")  
        else:  
            print("Invalid action! You lose your turn.")  
            continue  

    elif boss_mode == "attack":  
        if action == "2":  
            print("You brace yourself for the incoming attack.")  
            # Boss attacks since the player is defending  
            damage_taken = int(boss_attack_damage * defense_multiplier)  
            player_health -= damage_taken  
            print(f"{boss_name} attacks you with a demonic claw for {boss_attack_damage} damage! You defend and take {damage_taken} damage.")  
            # After attack, switch boss mode back to idle  
            boss_mode = "idle"  
        elif action == "1":  
            print("You choose to attack!")  
            # Player attacks, and the boss also attacks back  
            player_health -= strong_attack_damage  # Boss deals double damage  
            print(f"{boss_name} counterattacks you with a demonic claw for {strong_attack_damage} damage! You deal {player_attack_damage} damage but the boss takes no damage.")  
            # After attack, switch boss mode back to idle  
            boss_mode = "idle"  
        else:  
            print("Invalid action! Please choose to attack or defend.")  
            continue  

# Battle result  
if player_health <= 0:  
    print("\nYou have been defeated! Better luck next time.")  
else:  
    print(f"\nYou have defeated {boss_name}! Victory is yours!")