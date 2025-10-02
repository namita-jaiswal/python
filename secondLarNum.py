def second_largest():
    cocoa=[2,4,7,3,6,9]

    if cocoa[0]>cocoa[1]:
        first=cocoa[0]
        second=cocoa[1]

    else:
        first=cocoa[1]
        second=cocoa[0]


    for i in cocoa[2:]:

        if i>first:
            second=first
            first=i

        elif i>second and i!=first:
            second=i

    return second

print(second_largest())