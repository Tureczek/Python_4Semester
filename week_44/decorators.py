import functools # used to help in the other class on line 139
import time # Used for time decorator
import random # for Plugin examples

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


""" Time decorator that will mesure the time a function takes to exercut0e """
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

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

""" Getting a modified version on line 133

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs): # takes arbitrary arguments and returns the value of the decorated function
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
"""
"""
There are a few subtle things happening in the repeat() function:

1 Defining decorator_repeat() as an inner function means that repeat() will refer to a function object—decorator_repeat. 
Earlier, i used repeat without parentheses to refer to the function object. 
The added parentheses are necessary when defining decorators that take arguments in the fancy_decorators.

2 The num_times argument is seemingly not used in repeat() itself. But by passing num_times a closure is created 
where the value of num_times is stored until it will be used later by wrapper_repeat().

"""


# Define decorators that can be used both with and without arguments
""" BOILERPLATE!
def name(_func=None, *, kw1=val1, kw2=val2, ...):  # 1
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    if _func is None:
        return decorator_name                      # 2
    else:
        return decorator_name(_func)               # 3
"""
"""
1    If name has been called without arguments, the decorated function will be passed in as _func. If it has 
        been called with arguments, then _func will be None, and some of the keyword arguments may have been changed
        from their default values. The * in the argument list means that the remaining arguments can’t be called as 
        positional arguments.
        
2    In this case, the decorator was called with arguments. Return a decorator function that can read and return a function.

3    In this case, the decorator was called without arguments. Apply the decorator to the function immediately.

Using the above boilerplate on repeat function:
"""


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

# Stateful Decorator that keep track of state ex number of times a function is called

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1 #
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
"""
The state—the number of calls to the function—is stored in the 
function attribute .num_calls on the wrapper function.
"""

# Classes as Decorators
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)