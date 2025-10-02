x=int(input("Enter any two digit number")) #q1
rev=0
original=x
i=0
while x>0:
    digit=x%10
    rev=rev*10+digit
    x=x//10
add=rev+original
print(add)

a=int(input("Enter a number: ")) #q2
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
if a>0 and b>0 and c>0:
    print(max(a,b,c))
elif a<0 and b<0 and c<0:
    print(min(a,b,c))
else:
    print(a+b+c)

n=int(input("Enter a number: "))#q3
if n<0:
    print("Invalid input")
sum1=n*(n+1)//2
print("sum of 1 to",n, "is",sum1)



x1=int(input("Enter a number: "))#q5
y1=float(input("Enter a number: "))
z1=int(input("Enter a number: "))
intPart=x1*int(y1)
fractionalPart=z1*(y1-int(y1))
print("the final result is: ",round(intPart+fractionalPart,3))