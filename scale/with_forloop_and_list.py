def create_monster():
    name = input("What's the monster's name? ")
    hp = int(input("What's the monster's HP? "))
    attack = int(input("What's the monster's attack power? "))
    return {"name": name, "hp": hp, "attack": attack}

monsters = []
num = int(input("How many monsters do you want to create? "))

for i in range(num):
    print(f"\nCreating monster {i + 1}:")
    monster = create_monster()
    monsters.append(monster)

print("\nSummary of Monsters:")
for idx, monster in enumerate(monsters, start=1):
    print(f"{idx}. {monster['name']} - HP: {monster['hp']}, Attack: {monster['attack']}")
