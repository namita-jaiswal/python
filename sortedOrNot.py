arr=[6,5,8,4,6,5,1,6,5,4]
is_sorted=False
for i in range(1,len(arr)):
    if arr[i]>=arr[i-1]:
        is_sorted=False
        break

if is_sorted:
    print("sorted")
else:
    print("unsorted")