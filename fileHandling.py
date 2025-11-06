with open("file.txt","r") as f:
    
    # content=f.read()
    # print(content)

    line1=f.readline()
    print(line1)
    line2=f.readline()
    print(line2)

    # lines=f.readlines()
    # print(lines)

# with open("file.txt","w") as f:
#     f.write("This is newly added")

# with open("file.txt", "a") as file:
#     file.write("\nThis line is appended")

# lines=["This is namita\n", "This is himanshi\n", "This is priyanshu\n"]
# with open("file.txt","w") as f:
#     f.writelines(lines)
