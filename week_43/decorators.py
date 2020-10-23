import functools # used to help in the other class on line 139
import time # Used for time decorator

"""
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice()
"""
"""
def do_twice(func):
    def wrapper_do_twice(*args, **kwarks):
        func(*args, **kwarks)
        func(*args, **kwarks)
    return wrapper_do_twice
"""

def do_twice(func):
    @functools.wraps(func) #linked to the import functools line 127 in functions & decorators
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


"""
#Good boilerplate template for building more complexe decorators:
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = finc(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
"""


""" Time decorator that will mesure the time a function takes to exercute """
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

""" Debugging decorator code """
def debug(func):
    """ Print the function signature and return value """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                       # 1
        kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()] # 2
        signature = ", ".join(args_repr + kwargs_repr)            # 3
        print(f"Calling {func.__name__!r}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")            # 4
        return value
    return wrapper_debug
"""
    1. Create a list of the positional arguments. Use repr() to get a nice string representing each argument.
    2. Create a list of the keyword arguments. The f-string formats each argument as key=value where the !r 
       specifier means that repr() is used to represent the value.
    3. The lists of positional and keyword arguments is joined together to one signature string with each argument separated by a comma.
    4. The return value is printed after the function is executed.
"""
