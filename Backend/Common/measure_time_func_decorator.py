import time
from functools import wraps


def measure_time_func(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Starting execution func {func.__name__} : ...")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time : {float(end - start)} seconds")
        return result

    return wrapper
