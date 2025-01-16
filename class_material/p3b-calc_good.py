# Program to calculate speed based on distance and time  

# Prompt the user to enter the distance  
distance = float(input("Enter the distance traveled (e.g., meters, kilometers): "))  

# Prompt the user to enter the time  
time = float(input("Enter the time taken (e.g., seconds, hours): "))  

# Calculate the speed using the formula Speed = Distance / Time  
speed = distance / time  

# Display the result to the user  
print(f"The speed is: {speed:.2f} units per unit of time")