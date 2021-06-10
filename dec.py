import time
from functools import wraps

def cal_time(any_fucntion):
    @wraps(any_fucntion)
    def wrapper_func(*args,**kwargs):
        print(f'Executing ....{any_fucntion.__name__}')
        t1=time.time()
        returned_value = any_fucntion(*args,**kwargs)
        t2=time.time()
        total_time = t2-t1
        print(f'your function took {total_time} seconds to run')
        return returned_value
    return wrapper_func

@cal_time
def square_finder(n):
    return [i**2 for i in range (1,n+1)]

square_finder(1000)




