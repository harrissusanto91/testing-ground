# Input coefficients  
a = float(input("Enter coefficient a: "))  
b = float(input("Enter coefficient b: "))  
c = float(input("Enter coefficient c: "))  

# Calculate the discriminant  
D = b**2 - 4 * a * c  

# Calculate the two solutions using the quadratic formula  
x1 = (-b + D**0.5) / (2 * a)  
x2 = (-b - D**0.5) / (2 * a)  

# Output the solutions  
print(f"The roots of the equation are: {x1} and {x2}")  