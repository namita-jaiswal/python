import math#Q5
import random
for i in range(1,201):
    if i%9==0 or math.sqrt(i)**2==i:
        print(i)

s=0 #Q1
for j in range(1,501):
    if j%7==0 and j%5!=0:
        for count in str(j):
            s+=int(count)
            if s%2==0:
                print(j)
                if s==20:
                    break


