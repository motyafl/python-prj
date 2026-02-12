import numpy as np
import matplotlib.pyplot as plot
import tools
plot.close('all') # remove old graphs

def f(x):
    return (4-x)*np.sin(2*x-3)+ \
            2*np.cos(3*x-4*np.sin(x-2))-3

a1 = -10
b1 = -8

a2 = -8
b2 = 7
e = 0.0001

xz1 = tools.bisect(f, a1, b1, e)
xz2 = tools.newton(f, b2, e)
xzs = np.array([xz1,xz2])
yzs = f(xzs)
print([xz1,yzs[0]])
print([xz2,yzs[1]])

X = np.arange(-10, 10.1, 0.1) # array of dots from -10 to 10 with step of 0.1, analogue of c array
Y = f(X)
plot.plot(X, Y)

plot.plot(xzs[0], yzs[0], '*b')
plot.plot(xzs[1], yzs[1], '*r')
plot.grid()
#plot.xlable('X') # why doesent work?
#plot.ylable('Y')
#plot.show()
plot.savefig("output.jpg")
