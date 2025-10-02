marks=[3,5,6, "harry", True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# Convert negative indexing into positive indexing.
print(marks[-3]) # Negative Indexing
print(marks[len(marks)-3])

if "harry" in marks:
    print("Yeah")
else:
    print("Nah")

if "arry" in "Harry":
    print(True)

print(marks[:]) # means [0:len(marks)]
print(marks[1:-2]) # last value is ignored
print(marks[1:4:2]) # Jumping Index [prints 1, jumps two, prints 4th, jumps two (including the previous) prints 7th]

list1=[i for i in range (21) if i%4==0] # List Comprehension
print(list1)