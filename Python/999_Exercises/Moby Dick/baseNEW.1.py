s = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"

counter - 0

for i in range (0, sentence):
    if s == "whale":
    print (counter)
        counter = counter + 1
        
counter = 0

#answer:

sentence = "whale hello there. Don't we all love whales? I absolutely love whales! whales are so huge!!!"
count = 0

for i in range (0, len(sentence)):
    if sentence [i:i+5] == "whale": 
        count = count + 1
        print (count)
    
count = 0
for line in f:
    sentence = line.strip ()
    for i in range (0, len(sentence)):
        print (count)
f.close()
