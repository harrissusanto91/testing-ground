def create_monster(name, hp, attack):
    print(f"A wild {name} appears!")
    return {"name": name, "hp": hp, "attack": attack}

def attack_monster(monster):
    monster["hp"] -= 10
    print(f"You attack the {monster['name']}! -10 HP")
    if monster["hp"] <= 0:
        print(f"The {monster['name']} is defeated!")
    else:
        print(f"{monster['name']} HP left: {monster['hp']}")

# Make a list of monsters
monster_list = [
    create_monster("Dinosaur", 30, 10),
    create_monster("Dragon", 50, 20),
    create_monster("Zombie", 20, 5),
    create_monster("Goblin", 25, 8),
    create_monster("Slime", 15, 3)
]

# Loop through each monster
for monster in monster_list:
    while monster["hp"] > 0:
        input("Press Enter to attack...")
        attack_monster(monster)
    print()  # empty line for spacing

print("All monsters defeated! You win!")