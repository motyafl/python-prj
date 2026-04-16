import numpy as np
import matplotlib.pyplot as plot
import tools
import time
plot.close('all') # remove old graphs

def f(x):
    return (4-x)*np.sin(2*x-3)+ \
            2*np.cos(3*x-4*np.sin(x-2))-3

a1 = -10
b1 = -8

a2 = 0
b2 = 5
e = 0.0001
'''
before = time.time()
for i in range(1000):
    tools.bisect(f, a1, b1, e)
after = time.time()
print("Bisection: ", after-before)

before = time.time()
for i in range(1000):
    tools.newton(f, (a1+b1)/2, e)
after = time.time()
print("Newton: ", after-before)

before = time.time()
for i in range(1000):
    tools.bisect_fast(f, a1, b1, e)
after = time.time()
print("Faster Bisection: ", after-before)

before = time.time()
for i in range(1000):
    tools.newton_fast(f, (a1+b1)/2, e)
after = time.time()
print("Faster Newton: ", after-before)


# Local min
before = time.time()
for i in range(1000):
    tools.thrsect(f, a2, b2, e)
after = time.time()
print("Threesect: ", after-before)

'''

before = time.time()
for i in range(1000):
    tools.thrsect_middle(f, a2, b2, e)
after = time.time()
print("Threesect with middle: ", after-before)

before = time.time()
for i in range(1000):
    tools.goldenR(f, a2, b2, e)
after = time.time()
print("Golden Rule: ", after-before)

