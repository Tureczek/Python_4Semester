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
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
