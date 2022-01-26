# Calculating area of a rectangular by using function

# Define a function to calculate area
def areRect(side1 ,side2 ):
    area = side1 * side2
    return area

# Get the sides of the rectangular
side1 = int(input("Enter the side1 of the rectangular :"))
side2 = int(input("Enter the side2 of the rectangular :"))

# Call the function and print the area
area = areRect(side1 ,side2 )
print("Area of the rectangular is :",area)