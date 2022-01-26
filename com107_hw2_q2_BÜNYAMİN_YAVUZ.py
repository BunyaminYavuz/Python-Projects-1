# Palindrom

# Get the numbers
number1 = input("Enter a number which is 3 digit :")
number2 = input("Enter a number which is 3 digit :")

# Check the first and last digit of the numbers
a, b = int(number1) % 10 , int(number2) % 10
c, d = int(number1[0]),  int(number2[0])

# Convert the str to int
number1 = int(number1)
number2 = int(number2)

# If the both numbers are palindromic number make addition
if (a == c and b == d):
    print(number1 + number2)

# If only one of the numbers is palindromic make subtraction
elif (a == c or b == d):
    subtraction = number1 - number2
    if subtraction < 0:
        subtraction = -subtraction
    print(subtraction)

# If both of the numbers are not palindomic number make multiplication
else:
    print(number1 * number2)





