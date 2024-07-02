x = float(input("enter your number (float or int)"))
print("first number is",x)
y = float(input("enter your second number (float or int)"))
print("second number is",y)
operater = input("what do you want to do with the numbers")



if operater=="+" :
    print(x+y)
elif operater=="-" :
    print(x-y)
elif operater=="*" :
    print(x*y)
elif y == 0 and operater == "/":
    print("invalid operater")
    exit()
elif operater=="/" :
    print(x/y)



