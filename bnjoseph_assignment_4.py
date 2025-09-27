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

#2
#if statements to check gpa and effect study_hours, stress_level (right now), and social_points
if current_gpa < 2.1 and current_gpa >= 1.0:
    study_hours = study_hours * 1.5
    stress_level += study_hours * 10
    social_points += 3
elif current_gpa < 3.5 and current_gpa >= 2.1:
    study_hours = study_hours * 1.25
    stress_level += study_hours * 10
    social_points += 2
else:
    study_hours = study_hours * 1
    stress_level += study_hours * 10
    social_points += 1
#display values
print("Study Hours:", study_hours)
print("Stress Level:", stress_level)
print("Social Points:", social_points)

#3
#initialize study_options
study_options = ["Programming", "Math", "English", "History"]
#get option
option = input()
#if statements for printing information on option
if option in study_options:
    print("Options:", option, "available.")
elif option not in study_options:
    print("Options:", option, "not available.")
if option == "Programming" or option == "Math":
    print("Stem")
if option is not "Programming" and option is not "Math":
    print("Boring Person")

#4
# display final options
print("A) Study")
print("B) Party")
print("C) Sleep")
#new gpa
gpa = current_gpa + study_hours / 15
if gpa > 4.0:
    gpa = 4.0
#get last choice
last_choice = input()
#nested statements
if last_choice == "A":
    study_hours += 10
    if gpa >= 3.5:
        print("Scholar")
    elif social_points >= 12:
        print("Party away your sorrows for academic failures")
    else:
        print("Unremarkable Academic")
elif last_choice == "B":
    social_points += 10
    if gpa >= 3.5:
        print("Sleepy intellectual")
    elif social_points >= 12:
        print("Center of the Party")
    else:
        print("Unremarkable Party Goer")
elif last_choice == "C":
    if gpa >= 3.5:
        print("Sleepy intellectual")
    elif social_points >= 12:
        print("Sleep and Party")
    else:
        print("Unremarkable")
else:
    print("Input is invalid")