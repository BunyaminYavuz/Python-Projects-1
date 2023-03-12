# Reverse the text
text = input("Write some textual item :")

# List of the article words
words = []


for i in text.split(" "):
    words.append(i)

for j in words:
    print(j[::-1])



