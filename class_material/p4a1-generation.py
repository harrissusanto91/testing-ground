# Step 1: Prompt the user for their birth year and convert to integer  
birth_year = int(input("Please enter your birth year (e.g., 1990): "))  

# Step 2: Determine the generation based on the birth year  
if birth_year < 1946:  
    generation = "Silent Generation"  
elif birth_year < 1965:  
    generation = "Baby Boomer"  
elif birth_year < 1981:  
    generation = "Generation X"  
elif birth_year < 1997:  
    generation = "Millennial"  
elif birth_year < 2013:  
    generation = "Generation Z"  
else:  
    generation = "Generation Alpha"  

# Step 3: Print the identified generation  
print(f"You belong to: {generation}")