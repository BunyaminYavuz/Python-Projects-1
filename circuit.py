# Calculator of the flow

# Get the volt and resistance for finding the flow
v = float(input("Enter tha value of the volt :"))

r = float(input("Enter tha value of the resistance :"))


while r == 0 :
    r = float(input("Resistance cannot be equal to 0,please enter a value which is different from 0 :"))
    if r != 0 :
        break

# Formula of curcuit
ı = v / r

print("The flow of the system is ",ı)
