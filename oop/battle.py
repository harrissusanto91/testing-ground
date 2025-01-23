import random  

class Character:  
    def __init__(self, name, health, strength):  
        self.name = name        # Name of the character  
        self.health = health    # Health points  
        self.strength = strength  # Attack strength  

    def attack(self, enemy):  
        """Attack the specified enemy."""  
        damage = random.randint(1, self.strength)  
        enemy.take_damage(damage)  
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")  

    def take_damage(self, damage):  
        """Reduce health by damage taken."""  
        self.health -= damage  
        print(f"{self.name} takes {damage} damage and now has {self.health} health.")  

    def is_alive(self):  
        """Check if the character is still alive."""  
        return self.health > 0  

class Enemy:  
    def __init__(self, name, health, strength):  
        self.name = name        # Name of the enemy  
        self.health = health    # Health points  
        self.strength = strength  # Attack strength  

    def attack(self, character):  
        """Attack the player character."""  
        damage = random.randint(1, self.strength)  
        character.take_damage(damage)  
        print(f"{self.name} attacks {character.name} for {damage} damage!")  

    def take_damage(self, damage):  
        """Reduce health by damage taken."""  
        self.health -= damage  
        print(f"{self.name} takes {damage} damage and now has {self.health} health.")  

    def is_alive(self):  
        """Check if the enemy is still alive."""  
        return self.health > 0  

def main():  
    # Create the player character  
    player = Character(name="Hero", health=100, strength=15)  
    
    # Create a list of enemies  
    enemies = [  
        Enemy(name="Goblin", health=30, strength=5),  
        Enemy(name="Orc", health=50, strength=10),  
        Enemy(name="Dragon", health=80, strength=15)  
    ]  

    # Battle loop  
    while player.is_alive() and any(enemy.is_alive() for enemy in enemies):  
        # Display player status  
        print(f"\n{player.name}'s Health: {player.health}")  
        print("Enemies:")  
        for enemy in enemies:  
            if enemy.is_alive():  
                print(f"{enemy.name} - Health: {enemy.health}")  

        # Player chooses an enemy to attack  
        enemy_choice = int(input("Choose an enemy to attack (0: Goblin, 1: Orc, 2: Dragon): "))  
        if 0 <= enemy_choice < len(enemies) and enemies[enemy_choice].is_alive():  
            player.attack(enemies[enemy_choice])  

            # Enemies attack the player  
            for enemy in enemies:  
                if enemy.is_alive():  
                    enemy.attack(player)  

    # Battle outcome  
    if player.is_alive():  
        print(f"\n{player.name} has defeated all enemies!")  
    else:  
        print(f"\n{player.name} has been defeated!")  

if __name__ == "__main__":  
    main()