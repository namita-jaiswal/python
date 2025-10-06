import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resullt = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} ran in {end - start} time.")     
        return resullt
    return wrapper

@timer # this function will always go through the timer function
def example_function(n):
    time.sleep(n)
    return n

example_function(2)