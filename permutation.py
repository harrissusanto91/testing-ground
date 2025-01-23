from itertools import permutations  

def main():  
    # Input from the user  
    user_input = input("Enter numbers separated by spaces: ")  
    
    # Split the input string into individual numbers  
    numbers = user_input.split()  
    
    # Generate unique permutations using a set  
    unique_permutations = set(permutations(numbers))  
    
    # Print all unique permutations  
    print("All possible unique permutations:")  
    for perm in unique_permutations:  
        print(' '.join(perm))  

# Entry point of the program  
if __name__ == "__main__":  
    main()