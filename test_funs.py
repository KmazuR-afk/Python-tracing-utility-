import time
import math

def fun_1():
    res=0
    for i in range(100):
        res=res+i
    return res

def fun_2():
    time.sleep(0.8)
    return 'Done waiting - time to work\n'

def fun_3(x):
    return math.sin(x)
