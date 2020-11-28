import time
import functools

# Print runtime of the decorated function
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args):
        start_time = time.pref_counter()
        value = func(*args)
        end_time = time.pref_counter()
        runtime = end_time - start_time
        print(f'Finished {func.__name__!r} in {runtime:.4f} seconds:')
        return value
    return wrapper_timer