# Name and Id of the company workers

number = int(input("Enter the number of the workers :"))
# name_ID = input("Enter your name and ID :")

workers = []

cnt = 1

while cnt <= number :
    name_ID = input("Enter your name and ID :")
    workers.append(name_ID)
    cnt = cnt + 1

# print(workers)
for i in workers :
    print(i)
