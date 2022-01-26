# Perfect Divisor

# List of divisors
exact_divisors = []

# Fuction of divisor finder
def exact_divisor(number):
    for i in range(1,number + 1):
        if number % i == 0:
            exact_divisors.append(i)
    print(exact_divisors)

# Taking target number
exact_divisor(number = int(input("Enter a number : ")))

