# Generators

import time
def compute():
    l = []
    for i in range(10):
        time.sleep(.5)
        l.append(i)

    return l

compute()
