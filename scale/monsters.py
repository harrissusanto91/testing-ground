def create_monster():
    name = input("What's the monster's name? ")
    hp = int(input("What's the monster's HP? "))
    attack = int(input("What's the monster's attack power? "))
    print(f"Monster created: {name}, HP: {hp}, Attack: {attack}")
    print()

# Create first monster
print("Let's create the first monster!")
create_monster()

# Create second monster
print("Let's create the second monster!")
create_monster()