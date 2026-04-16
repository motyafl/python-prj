import numpy as np
import math as m
import matplotlib.pyplot as plot
import tools
import time
plot.close('all') # remove old graphs


def f(x):
    return (4-x)*np.sin(2*x-3)+ \
            2*np.cos(3*x-4*np.sin(x-2))-3
#f1 = lambda x: -f(x) #this lambda function just returns what you need, in our case it is f function

def ft(x):
    return x*x
# Fiding roots
a1 = -10
b1 = -8

# Local minimum and maximum
a2 = 1
b2 = 5

e = 0.0001

# Finding roots
xz1 = tools.bisect(f, a1, b1, e)
xz2 = tools.newton(f, (a1+b1)/2, e)

# Local min and max
xz3 = tools.revstep(f, a2, e*100, e)
xz4 = tools.goldenR(lambda x: -f(x), a2, b2, e)
# Here it is better to temporary write lambda function, not making a new function to find maximum

xzs = np.array([xz1,xz2, xz3, xz4])
yzs = f(xzs)
print([xz1,yzs[0]])
print([xz2,yzs[1]])
print([xz3,yzs[2]])
print([xz4,yzs[3]])

X = np.arange(-10, 10.1, 0.1) # array of dots from -10 to 10 with step of 0.1, analogue of c array
Y = f(X)
plot.plot(X, Y)

plot.plot(xzs[0], yzs[0], '*b')
plot.plot(xzs[1], yzs[1], '*r')
plot.plot(xzs[2], yzs[2], '*g')
plot.plot(xzs[3], yzs[3], '*y')
plot.grid()
plot.xlabel('X')
plot.ylabel('Y')
#plot.show()
plot.savefig("output.jpg")

#Integration
a = 0
b = 1
st = 0.0001

Sf = tools.stepforw(ft, a, b, st)
Sb = tools.stepback(ft, a, b, st)
S = tools.stepfull(ft, a, b, st)

print ("\nStep forward: ", Sf, "\nStep backward: ", Sb, "\nFull step: ", (Sf+Sb)/2, "\nFaster full step:", S)

Sm = tools.midpoint(ft, a, b, st)
print ("Midpoint:", Sm)
