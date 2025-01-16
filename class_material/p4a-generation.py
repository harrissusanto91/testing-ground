# Input: Get the user's year of birth  
year_born = int(input("Please enter your year of birth (e.g., 1990): "))  

# Initialize variables for generation and fun fact  
generation = ""  
fun_fact = ""  

# Determine the generation and provide a fun fact (from newest to oldest)  
if year_born >= 2013:  
    generation = "Generation Alpha"  
    fun_fact = "Generation Alpha is still growing up, but they are expected to be the most technologically immersed generation yet."  
    
elif year_born >= 1997:  
    generation = "Generation Z (Gen Z)"  
    fun_fact = "Gen Z is considered digital natives, having grown up with smartphones, and they are known for their activism and social awareness."  
    
elif year_born >= 1981:  
    generation = "Millennials (Gen Y)"  
    fun_fact = "Millennials are the first generation to grow up with the Internet and are known for their focus on social issues."  
    
elif year_born >= 1965:  
    generation = "Generation X"  
    fun_fact = "Generation X is often referred to as the 'forgotten generation' and is known for its independent nature and embracing technology."  
    
elif year_born >= 1946:  
    generation = "Baby Boomers"  
    fun_fact = "Baby Boomers were known for their post-war optimism and having a large impact on music with artists like The Beatles."  
    
else:  # Anyone born before 1946  
    generation = "an unknown generation"  
    fun_fact = "Anyone born before 1946 is part of a generation that doesn't have a defined name, but they certainly shaped the world!"  

# Output: Display the generation and fun fact  
print(f"You were born in the year {year_born}, which makes you part of {generation}.")  
print(fun_fact)