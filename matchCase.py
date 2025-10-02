x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("x=0")
    case 4:
        print("x=4")
# underscore is used for default case
    case _ if x !=90:
        print(x, "not equal to 90")
    case _ if x !=80:
        print(x, "not equal to 80")
    case _:
        print(x)