fav = (input ("In a sentence, write out your favorite number (1-9): "))

age = int(input ("How old are you?:  "))

y = 0
s= 1
final = 0

for i in range (0, len(fav)) : 
    final = fav [y : s]
    y = y + 1
    s = s + 1

if ((final[y : s]) == int):
        final = (final[y: len(final)])
        print (name[0 : y])           

ans = final * age
print (ans)