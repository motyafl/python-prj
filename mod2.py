import numpy as np
import matplotlib.pyplot as plot
import tools2
import time

import functools #memorizing
#import numba #predcompiling

plot.close('all') # remove old graphs

X = [1, 2, 3]
Y = [2.5, 1, 2]

f = lambda x: tools2.lagrange(x, X, Y)

x = np.arange(1, 3.1, 0.1) #making a line on a plot instead of one dot
y = f(x) #tools2.lagrange(x, X, Y)

xext = 4
yext = f(xext)
print("Lagranges Interpolation:\n", y)

#plot.plot(X, Y, 'ro')
#plot.plot(x, y, 'md')
#plot.plot(xext, yext, 'rp')

@np.vectorize #puts function into decorator and make it ipossifle to call fdec, only vectorised  function, with the same name
def f_vec(x): #fdec(x)
    if x > 0:
        return x*x
    else:
        return -x

#f_vec = np.vectorize(f_dec) #now we can pass aerays in fdec this function is decorator-function
xvec = np.arange(-1, 1, 0.001) 
yvec = f_vec(xvec)

#plot.plot(xvec, yvec, 'b.')

plot.grid()
plot.xlabel('X')
plot.ylabel('Y')
#plot.show()
#plot.savefig("output.jpg")

def factorial(n):
    if n > 0:
        return n*factorial(n-1)
    else:
        return 1

F = factorial(5)
print("Factorial: ", F)

@functools.cache #memoizing
#@numbo.njit #predcompiling
def fibo(n):
    if n > 2:
        return n+fibo(n-1)
    else:
        return 1

Fi = fibo(150)
print("Fibonacchi: ", Fi)

## APROXIMATION

X = np.array([1, 2, 3, 4, 5, 6])
Y = np.array([1, 1.3, 1.7, 2.1, 2.8, 3])

x = np.linspace(min(X), max(X), 100)

A = tools2.approximate_line(X, Y)
f1 = lambda x: A[0]+A[1]*x
y = f1(x)
R_1 = sum((Y - f1(X))**2)

plot.plot(x, y)

print("Line Approximation: ", "\nX:", X, "\nY:", Y, "\nA:", A)

A_p = tools2.approximate_parabol(X, Y)
f1_p = lambda x: A_p[0]+A_p[1]*x + A_p[2]*x*x
y_p = f1_p(x)
R_p = sum((Y - f1_p(X))**2)

plot.plot(x, y_p)

print("Parabolic Approximation: ", "\nX:", X, "\nY:", Y, "\nA:", A_p)

A_p5 = tools2.approximate_poly(X, Y, 5)
f1_p5 = lambda x: A_p5[0]+A_p5[1]*x + A_p5[2]*x*x + A_p5[3]*x**3 + A_p5[4]*x**4 + A_p5[5]*x**5 
y_p5 = f1_p5(x)
R_p5 = sum((Y - f1_p5(X))**2)

plot.plot(x, y_p5)

print("Poly Approximation: ", "\nX:", X, "\nY:", Y, "\nA:", A_p5)

plot.plot(X, Y, "*r")
plot.legend([f'Line, R={R_1:.3f}',
             f'Parabol, R={R_p:.3f}',
             f'Poly, R={R_p5:.3f}'])
plot.savefig("output1.jpg")

plot.close('all') # remove old graphs
# 3D graphs amd local MIN/MAX in 3D
'''
def f(x):
    return (x[0]**2 + x[1] - 11)**2 + (x[1]**2 + x[0] - 7)**2

x1_rule = np.linspace(-5, 5, 101) # in interval -5 to 5 with 101 values 
x2_rule = np.linspace(-5, 5, 101)
x1,x2 = np.meshgrid(x1_rule, x2_rule) # just two linspaces wont work we need to interate througt all ys with all xs
X = [x1, x2]
Y = f(X)

#plot.figure() # window
#ax = plot.axes(projection='3d') # axis on full window

# figure and axes will be donr automatically only in 2d axes space

#ax.plot_surface(x1, x2, Y) # plot.gca() find and plot in prevous axes, or just plot ax as a pointer

ax1 = plot.subplot(2, 2, 2, projection='3d') # same as plot.axis only plots in certain area
ax1.set_title('abc')
ax2 = plot.subplot(2, 2, 4, projection='3d') # same as plot.axis only plots in certain area
ax3 = plot.subplot(1, 2, 1) # линии уровня

ax1.plot_surface(x1, x2, Y, cmap='plasma') # plot ax as a pointer in certain area # plasma is color map there are different types
ax2.plot_wireframe(x1, x2, Y, color='pink') # plot ax as a pointer in certain area
ax3.contour(x1, x2, Y, levels=15)

def fgrad(x):
    return np.array([4*x[0] * (x[0]**2 + x[1] - 11) + 2 * (x[1]**2 + x[0] - 7), 
                     2*(x[0]**2 + x[1] - 11) + 4*x[1]*(x[1]**2 + x[0] - 7)])

h = 1
e = 0.001
# xz1 = [0, 0]
# xmin = tools2.grad_method(f, fgrad, xz1, h, e)
# ax3.plot(xmin[0], xmin[1], 'r*')

xzs = [[2,2],[2,-2],[-2,2],[-2,-2]]
xmins = []
for i, xz in enumerate(xzs):
    xmins.append(tools2.grad_method(f, fgrad, xz, h, e))
    ax3.plot(xmins[i][0], xmins[i][1],'r*')

xzm = [0, 0]
#xmax = tools2.grad_method(lambda x: -f(x), lambda x: -fgrad(x), xzm, h, e)
xmax = tools2.easy_grad_method(lambda x: -f(x), xzm, h, e)
ax3.plot(xmax[0], xmax[1], 'b*')

plot.savefig("output.jpg")
'''


# Nonlinear system of equations

def f1up(x):
    return +np.sqrt(9-x*x)

def f1down(x):
    return -np.sqrt(9-x*x)

def f2up(x):
    return +np.sqrt((4-3*x)/2)

def f2down(x):
    return -np.sqrt((4-3*x)/2)

def f(x):
    f1 = x[0]**2 + x[1]**2 - 9
    f2 = 3*x[0] + 2*x[1]**2 - 4
    return np.array([f1,f2])

def J(x):
    df1_dx1 = 2*x[0]
    df1_dx2 = 2*x[1]
    df2_dx1 = 3
    df2_dx2 = 4*x[1]
    return np.array([[df1_dx1, df1_dx2],
                    [df2_dx1, df2_dx2]])

x1 = np.linspace(-3, 3, 121)
x2_up = f1up(x1)
x2_down = f1down(x1)

x12 = np.linspace(-3, 4/3, 121)
x22_up = f2up(x12)
x22_down = f2down(x12)

e = 0.001
xzero = np.array([0, 1])
xres = tools2.newton_rafson(f, J, xzero, e)
'''
plot.plot(x1, x2_up, 'b')
plot.plot(x1, x2_down, 'b')
plot.plot(x12, x22_up, 'r')
plot.plot(x12, x22_down, 'r')

plot.plot(xres[0], xres[1], 'md')
'''

x_rule = np.linspace(-3,3,101)
x1g,x2g = np.meshgrid(x_rule, x_rule)
Z1,Z2 = f([x1g,x2g])

ax1u=plot.subplot(2,3,1)
ax1d=plot.subplot(2,3,4, projection='3d')
ax2=plot.subplot(1,3,2)
ax3u=plot.subplot(2,3,3)
ax3d=plot.subplot(2,3,6, projection='3d')

ax2.plot(x1, x2_up, 'b')
ax2.plot(x1, x2_down, 'b')
ax2.plot(x12, x22_up, 'r')
ax2.plot(x12, x22_down, 'r')

ax2.plot(xres[0], xres[1], 'md')

ax1u.contour(x1g, x2g, Z1)
ax3u.contour(x1g, x2g, Z2)


ax1d.plot_surface(x1g, x2g, Z1)
ax3d.plot_surface(x1g, x2g, Z2)

# In polars
#angle = np.arange(0, 2*np.pi + np.pi/16, np.pi/16)
#radius = 3*np.ones(len(angle))
#plot.polar(angle, radius)

plot.savefig("output.jpg")
