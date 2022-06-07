thislist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input("How many numbers would you like to see: "))
import random


for i in range (0, num):
    print (thislist[random.randrange(10)])