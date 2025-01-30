# Ask the user for the number of students
num_students = int(input("How many students? "))

scores = []  # List to store scores

# Get scores from the user
for i in range(num_students):
    score = int(input(f"Enter score for student {i+1}: "))
    scores.append(score)

print("\nStudent Scores and Categories:")
for score in scores:
    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 50:
        category = "Average"
    else:
        category = "Needs Improvement"
    
    print(f"{score} -> {category}")
