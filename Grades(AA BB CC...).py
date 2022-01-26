# Grades calculator

# To take input as many as number of students
number_of_students = int(input("Enter the number of students: "))

letter_grades = []

# In while loop taking (name, grades)
while number_of_students > 0:

    names_student = input("Enter the name and surname of the student: ")

    achievement_grade = int(input("Enter the achievement grade of the student: "))

    final_grade = int(input("Enter the final grade of the student:"))

    overall_grade = achievement_grade * 0.4 + final_grade * 0.6

    letter_grade = ""

    if 85 <= overall_grade <= 100 :
        letter_grade = "AA"
    elif 70 <= overall_grade < 85 :
        letter_grade = "BA"
    elif 60 <= overall_grade < 70 :
        letter_grade = "BB"
    elif 50 <= overall_grade < 60 :
        letter_grade = "CB"
    elif 40 <= overall_grade < 50 :
        letter_grade = "CC"
    elif 0 <= overall_grade < 40 :
        letter_grade = "FF"

    letter_grades.append(names_student + " : " + str(overall_grade) + "/" + letter_grade)

    number_of_students = number_of_students - 1

print(letter_grades)