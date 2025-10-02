slurp=[0,1,2,3,4,5,6,9,7,8]
lar=slurp[3]
sort=sorted(slurp)
print(sort)

for i in slurp:
    if i>lar:
        lar=i
print(lar)