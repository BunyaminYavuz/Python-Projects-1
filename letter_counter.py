# Letter counter

# Function
def find(word,letter):
    index = 0
    while index < len(word):
        if word[index] == letter :
            return index
        index = index + 1
    return -1

# Get the text and the aim letter which will be counted
text = input("Enter an any textual items :")

aim_letter = input("Enter which letter you want to count :")

# It counts the aim letter
print(find(text,aim_letter))