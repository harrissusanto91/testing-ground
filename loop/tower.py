# User input for height  
height = int(input("Enter the height of the pyramid: "))  

for i in range(height):  
    print(' ' * (height - i - 1), end='') # Print spaces   
    print('*' * (2 * i + 1)) # Print asterisks   