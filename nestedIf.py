# nested if
n = 0
if(n<0):
    print("Number is negative")
elif(n>0):
    if(n<=10):
        print("Number lies between 1-10")
    elif(n>=11 and n<=20):
        print("Number lies between 11 and 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero")