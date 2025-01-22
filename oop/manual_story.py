def main():
    new_room = create_room()
    print(f"you hace created {new_room.name} which is {new_room.description}")

class Room:
    def __init__(self,name,description):
        self.name = name
        self.description =description

def create_room():
    name = input("Name: ")
    description = input("Describe: ")
    return Room(name, description) 
    

main()