import numpy as np
import matplotlib.pyplot as plot
import tools
import time
plot.close('all') # remove old graphs

def f(x): # основная функция
    return -1 * np.exp(np.sin(x)) + 2*x*np.sin(np.exp(x-5)) \
            + 4*np.sin(x-1)

# Fiding roots
# Local minimum and maximum
# Ограничения для поиска корней/локальнях экстремумов
a1 = -5
b1 = 1

a2 = 1
b2 = 5
e = 0.001

a3 =-5 
b3 = 5

# Finding roots
xz1 = tools.bisect(f, a3, b3, e)
#xz1 = tools.newton(f, (a1+b1)/2, e)
xz2 = tools.newton(f, (a1+b1)/2, e)

# Local min and max
xz3 = tools.revstep(f, b2, e*100, e)
xz4 = tools.goldenR(lambda x: -f(x), a2, b2, e) # испоьзуем лямбда функцию для поиска максимума

xz5 = tools.revstep(f, b1, e*100, e)
xz6 = tools.goldenR(lambda x: -f(x), a1, b1, e) # испоьзуем лямбда функцию для поиска максимума

# Graph
xzs = np.array([xz1,xz2, xz3, xz4, xz5, xz6])
yzs = f(xzs)
print([xz1,yzs[0]])
print([xz2,yzs[1]])
print([xz3,yzs[2]])
print([xz4,yzs[3]])
print([xz5,yzs[4]])
print([xz6,yzs[5]])

X = np.arange(-5, 5.1, 0.1) # ограничения для графика
Y = f(X)
plot.plot(X, Y)

plot.plot(xzs[0], yzs[0], '*r') # root 
plot.plot(xzs[1], yzs[1], '*b') # root
plot.plot(xzs[2], yzs[2], '*g') # local MIN
plot.plot(xzs[3], yzs[3], '*y') # local MAX
plot.plot(xzs[4], yzs[4], '*g') # local MIN 
plot.plot(xzs[5], yzs[5], '*y') # local MAX
plot.grid()
plot.xlabel('X')
plot.ylabel('Y')
plot.show()
#plot.savefig("output.jpg")

#Integration
a = -5
b = 5
st = 0.001

Sf = tools.stepforw(f, a, b, st)
Sb = tools.stepback(f, a, b, st)
S = tools.stepfull(f, a, b, st)

print ("\nStep forward: ", Sf, "\nStep backward: ", Sb, "\nFull step: ", (Sf+Sb)/2)

Sm = tools.midpoint(f, a, b, st)
print ("Midpoint:", Sm)
