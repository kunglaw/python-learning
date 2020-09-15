if 1 < 2:
    print("yes its true")

name = "dimas"
age = 28

if name != "":
    print("welcome "+name)
    if age > 17:
        print("you already have an ID")
    else:
        print("sorry sir you dont have an ID")
else:
    print("Sorry sir, put your name")

num = 15

if num % 5 == 0:
    print(str(num)+" adalah Bilangan kelipatan 5")
elif num % 3 == 0:
    print(str(num)+" adalah bilangan kelipatan 3")
elif num % 2 == 0:
    print(str(num)+" adalah bilangan genap")
