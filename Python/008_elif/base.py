one = int(input("Choose a number: "))
two = int(input("Choose a second number: "))
three = input("Choose an operation: ")


an = one + two
ane = one - two
anes = one * two
anes = one / two

if (three == "+" ):
    print (str(one) + "+" + str(two) + "=" + str(an))
    
elif (three == "-" ):
    print (str(one) + "-" + str(two) + "=" + str(ane))
    
elif (three == "*" ):
    print (str(one) + "*" + str(two) + "=" + str(anes))
    
elif (three == "/" ):
    print (str(one) + "/" + str(two) + "=" + str(anes))