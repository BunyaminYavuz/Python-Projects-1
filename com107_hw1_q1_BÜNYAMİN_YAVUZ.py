# Calculator of the lowest grade

# Take the number of the inputs
N = int(input("Enter a number N :"))

cnt = 1

smallest = 100

# Geting input as many as N variable
while cnt <= N:
    grade = int(input("Grade :"))
    if grade < biggest:
        smallest = grade
    cnt = cnt + 1


print(smallest)
