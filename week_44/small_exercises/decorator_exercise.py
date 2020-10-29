import functools
from datetime import datetime
import time
import logging

logging.basicConfig(level=logging.INFO, filename='timeStamp.log')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def time_stamp(func):
    @functools.wraps(func)
    def wrapper_time_stamp(*args):
        wrapper_time_stamp.time_call = current_time
        print(f"Call at {wrapper_time_stamp.time_call} of {func.__name__!r}")
        logging.info(f"Call at {wrapper_time_stamp.time_call} of function {func.__name__!r} with the value {func(*args)!r}")
        return func(*args)
    wrapper_time_stamp.time_call = 0
    return wrapper_time_stamp


def print_twice(func):
    @functools.wraps(func)
    def wrapper_print_twice(*args):
        print(*args)
        print(*args)
    return wrapper_print_twice

def take_time(func):
    @functools.wraps(func)
    def wrapper_time(*args):
        start_time = time.perf_counter()
        value = func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_time



def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args):
        time.sleep(1)
        return func(*args)
    return wrapper_slow_down