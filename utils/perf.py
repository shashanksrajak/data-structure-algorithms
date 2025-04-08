import time

# decorator function to measure perf time


def perf_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time {end_time - start_time:.6f} seconds")
        return result
    return wrapper
