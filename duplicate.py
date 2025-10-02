# To return the number of unique elements in an array.

def duplicate():
    arr=[1,1,2,2,2,3,3,4]
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1
print(duplicate())