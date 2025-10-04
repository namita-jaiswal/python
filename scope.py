username="chaiaurcode"

def func():
    username = "chaiaurcode"

print(username)
func()


x=99 # global variable

def func2(y):
    z = x + y
    return z
y=1
res = func2(y)
print(res)


# def func3():
#     global x # bad practice
#     x=88

# func3()
# print(x)


def func4():
    x=88 # climbing

    def innerfn():
        print(x)
    return innerfn
result = func4()
result()

def chai(code):
    def actual(x):
        return x ** code
    return actual

f = chai(2)
g = chai(3)

print(f(3))
print(g(3))