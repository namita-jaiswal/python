string=input("Enter the string: ").upper()
def minion_game(string):
    vowels="AEIOU"
    kevsc=0
    stusc=0
    str_len=len(string)
    for i in range(str_len):
        if string[i] in vowels:
            kevsc+=kevsc+1
        else:
            stusc+=stusc+1
    if kevsc>stusc:
        print("Kevin",kevsc)
    elif stusc>kevsc:
        print("Stuart",stusc)
    else:
        print("Draw")
minion_game(string)
