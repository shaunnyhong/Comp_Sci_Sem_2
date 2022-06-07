first = (input("Enter first name and last: "))
y = 0
s = 1
for i in range (0, len(first)):
    letter = first [y : s]
    print (letter)
    y = y + 1
    s = s + 1

if ((first[y : s]) == " "):
    print (first[y: len(first)])
    print (name[0 : y])           