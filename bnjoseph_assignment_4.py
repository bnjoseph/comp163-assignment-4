#1
#initialization
student_name = "Bryce Joseph"
current_gpa = 3.4
study_hours = 1
social_points = 1
stress_level = 1
#display for options
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
#if statements
choice = input("Your choice: ")
if choice == "A":
    # Use comparison operators to check GPA and adjust variables
    study_hours = 12
elif choice == "B":
    # Different logic path
    study_hours = 15
elif choice == "C":
    # Heavy load - check if GPA >= 3.5 for different outcomes
    study_hours = 18
else:
    print("Input is invalid")