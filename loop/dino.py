# Initialize HP  
hp = 100  

print("Game Start")  

# Main game loop  
while hp > 0:  
    input("Press Enter to attack the dinosaur...")  
    hp -= 10  
    
    # Attack animation  
    print("Oww...")  
    print("HP is decreasing!")  
    print(f"Current HP: {hp}")  
    print("Dinosaur is idle.")  

# Game Over message  
print("Game Over! The dinosaur is defeated.")  