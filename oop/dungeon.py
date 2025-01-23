import random  

# Define enemy stats in a dictionary  
def create_enemy(name, health, attack):  
    return {  
        'name': name,  
        'health': health,  
        'attack': attack  
    }  

# Define player stats in a dictionary  
def create_player(name):  
    return {  
        'name': name,  
        'health': 100,  
        'attack': 10,  
        'inventory': []  
    }  

# Function to display room description and handle fights  
def enter_room(player, room):  
    print(room['description'])  
    if 'enemy' in room:  
        fight(player, room['enemy'], room)  
    else:  
        explore_room(player, room)  

# Function to manage the fight mechanics  
def fight(player, enemy, room):  
    print(f"A wild {enemy['name']} appears!")  
    while player['health'] > 0 and enemy['health'] > 0:  
        print("\nWhat will you do?")  
        print("1. Attack")  
        print("2. Run Away")  
        
        choice = input("Choose an option (1/2): ")  

        if choice == "1":  
            # Player attacks  
            enemy['health'] -= player['attack']  
            print(f"{player['name']} attacks {enemy['name']}! {enemy['name']} takes {player['attack']} damage!")  
            
            if enemy['health'] > 0:  
                # Enemy attacks  
                player['health'] -= enemy['attack']  
                print(f"{enemy['name']} attacks {player['name']}! {player['name']} takes {enemy['attack']} damage!")  
        elif choice == "2":  
            print(f"{player['name']} runs away from the {enemy['name']}!")  
            return  
        else:  
            print("Invalid choice, please choose again.")  

    if player['health'] > 0:  
        print(f"You defeated the {enemy['name']}!")  
        if 'item' in room:  
            player['inventory'].append(room['item'])  
            print(f"You found a {room['item']}!")  

# Function for exploring non-enemy rooms  
def explore_room(player, room):  
    print("\nWhat will you do?")  
    print("1. Search the room")  
    print("2. Leave the room")  
    
    choice = input("Choose an option (1/2): ")  
    
    if choice == "1":  
        if 'item' in room:  
            player['inventory'].append(room['item'])  
            print(f"You found a {room['item']}!")  
            del room['item']  # Remove item after collecting  
        else:  
            print("There's nothing interesting here.")  
    elif choice == "2":  
        print(f"You leave the {room['description']}.")  
    else:  
        print("Invalid choice, please choose again.")  

# Function to start the game  
def start_game():  
    player_name = input("Enter your name: ")  
    player = create_player(player_name)  

    rooms = [  
        {'description': "You are in a dark room.",   
         'enemy': create_enemy("Goblin", 30, 5),   
         'item': "health potion"},  
        {'description': "You enter a dimly lit cave.",   
         'enemy': create_enemy("Zombie", 20, 3)},  
        {'description': "You stumble into a hidden treasure room!",   
         'item': "gold coin"},  
        {'description': "You are in an ancient temple.",   
         'enemy': create_enemy("Skeleton", 40, 7)},  
        {'description': "You find yourself in a mysterious forest."}  
    ]  

    print(f"Welcome to the dungeon, {player['name']}!")  
    for room in rooms:  
        enter_room(player, room)  
        if player['health'] <= 0:  
            print("Game Over!")  
            break  

    if player['health'] > 0:  
        print(f"Congratulations, {player['name']}! You have completed the dungeon adventure.")  

if __name__ == "__main__":  
    start_game()