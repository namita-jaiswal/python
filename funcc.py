def average(a=9, b=1):
  print("The avg is", (a+b)/2)
average(4, 6) # default argument will be ignored
average(b=8, a=2)

def name(fname="Amy", mname="John", lname):
   print("Hello,", fname, mname, lname)
name("Ishika", "Agarwal", "Sinha")

def average(*number):
    pass

