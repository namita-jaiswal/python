a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if a>=18:
  print("Yes")
  print("You can drive")
  print("😊")
else:
  print("No")
  print("You cannot drive")
  print("😔")
# Indentation indicates that the code is being executed under if or else condition.
# Will only be printed if else condition is satisfied.

price = 210
budget = 300
if budget-price>=50:
    print("Buy the apples")
else:
    print("Exceeds the budget")