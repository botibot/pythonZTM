from time import time

def performance(func):
    def wrapper_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print (f'it took {t2-t1} s')
        return result
    return wrapper_func

@performance
def long_time():
    for i in range(1000000000):
        i*5

long_time()