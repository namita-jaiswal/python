# Strings are immutable
name = "Nam!taa a!"

# print(len(name))
# print(name.upper())
# print(name.lower())
# print(name.rstrip("!"))
# print(name.lstrip("N"))
# print(name.replace("a", "4"))
# print(name.split(" "))

heading = "introduction to python"
# print(len(heading))
# print(heading.center(50)) #adds (input space - length of string) number of space.
# print(name.count("a"))
# print(name.endswith("a!"))
# print(name.startswith("Nam"))
print(heading.endswith("ti", 4 , 10)) #python checks substring heading[4:10] oducti(it ends with ti)
# print(heading.find("ion")) #tells the position where it is stored in the string
# print(heading.find("lol")) #returns -1 cuz lol doesn't exist
# print(heading.index("intro")) #throws an error if false

alpha = "thatisamazing"
# print(alpha.isalnum()) #no spaces [A-Z, a-z, 0-9]
# print(alpha.isalpha()) #no numbers [A-Z, a-z]
# print(alpha.islower()) #bool
# print(alpha.isupper()) #bool
# print(alpha.isprintable()) #wouldn't be if there was \n or \" etc.

str1 = "        " #spaceBar
str2 = "      " #tabKey
# print(str1.isspace())
# print(str2.isspace())

title = "United Nations"
# print(title.istitle()) #first letter of all the words should be capital
# print(title.swapcase()) #uNITED nATIONS

title2 = "Her name is Aditi"
# print(title2.title()) # Her Name Is Aditi