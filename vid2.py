# Left rotate an array by 1 place: [2,3,4,5,1]

arr=[2,4,6,4,3,9]
temp=arr[0]
for i in range (1,len(arr)):
    arr[i-1]=arr[i]
arr[(len(arr))-1]=temp
print (arr)

# Left rotate an array by D places.

arey=[1,2,3,4,5,6,7]
temp1=[1,2,3]
D=3

for i in range (1,len(arey)):
     arey[(len(arey))-(D+1)]=arey[i]
print(len(arey))