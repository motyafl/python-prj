import numpy as np
import matplotlib.pyplot as plot
import tools2_test

plot.close('all') # remove old graphs

# Iterpolation
# Задание 1

X = [1, 2, 3, 4, 6, 7]
Y = [1.6, 1.7, 1.9, 2.2, 3.4, 5.8]

f = lambda x: tools2_test.lagrange(x, X, Y)

x = np.arange(0, 8.1, 0.01) #making a line on a plot instead of one dot
y = f(x) 

xext = 5
xext1 = 8
yext = f(xext)
yext1 = f(xext1)
print("Задание 1. Интерполяция Лагранжа :", "\nx*=5, y*=", yext, "\nx**=8, y**=", yext1)

plot.title("Задание 1")
plot.plot(x, y)#, 'md')
plot.plot(X, Y, 'ro')
plot.plot(xext, yext, 'bo')
plot.plot(xext1, yext1, 'bo')
plot.savefig("graphs/interpolation.jpg")

#plot.show()
plot.close('all') # remove old graphs

# APROXIMATION
# Задания 2 и 3

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([5389, 6343, 7497, 8672, 10131, 11917, 13584,\
              15770, 18328, 21102])

x = np.linspace(min(X), max(X), 100)

A_k = tools2_test.approximate_kr(X, Y)

f1_p = lambda x: A_k[0] + A_k[1]*x + A_k[2]*x*x + A_k[3]*np.exp(x) + A_k[4]*np.exp(-x) 
y_p = f1_p(x)
R_p = sum((Y - f1_p(X))**2)

X_pr = np.array([11, 12, 13])
Y_pr = f1_p(X_pr)

x_pr = np.linspace(10, 13, 100)
y_pr = f1_p(x_pr)

plot.title("Задания 2 и 3")
plot.plot(X, Y, "*r")
plot.plot(X_pr, Y_pr, "*g")
plot.plot(x, y_p)
plot.plot(x_pr, y_pr)

# Апроксимация для каждого из оставшихся 4 вариантов

A_k2 = tools2_test.approximate_kr2(X, Y)
f2_p = lambda x: A_k2[0] + A_k2[1]*x + A_k2[2]*x*x + A_k2[3]*np.sin(x) + A_k2[4]*np.cos(x) 

y_p2 = f2_p(x)
R_p2 = sum((Y - f2_p(X))**2)

Y_pr2 = f2_p(X_pr)

y_pr2 = f2_p(x_pr)

plot.plot(X, Y, "*r")
plot.plot(X_pr, Y_pr2, "*g")
plot.plot(x, y_p2)
plot.plot(x_pr, y_pr2)


A_k3 = tools2_test.approximate_kr3(X, Y)

f3_p = lambda x: A_k3[0] + A_k3[1]*x*x + A_k3[2]*x**4 + A_k3[3]*np.sin(x) + A_k3[4]*np.cos(x)

y_p3 = f3_p(x)
R_p3 = sum((Y - f3_p(X))**2)

Y_pr3 = f3_p(X_pr)

y_pr3 = f3_p(x_pr)

plot.plot(X, Y, "*r")
plot.plot(X_pr, Y_pr3, "*g")
plot.plot(x, y_p3)
plot.plot(x_pr, y_pr3)


A_k4 = tools2_test.approximate_kr4(X, Y)

f4_p = lambda x: A_k4[0] + A_k4[1]*x + A_k4[2]*x*x*x + A_k4[3]*x**5 + A_k4[4]*np.arctan(x) 

y_p4 = f4_p(x)
R_p4 = sum((Y - f4_p(X))**2)

Y_pr4 = f4_p(X_pr)

y_pr4 = f4_p(x_pr)

plot.plot(X, Y, "*r")
plot.plot(X_pr, Y_pr4, "*g")
plot.plot(x, y_p4)
plot.plot(x_pr, y_pr4)
plot.legend([f'Var1, R={R_p:.3f}',
             f'Var2, R={R_p2:.3f}',
             f'Var3, R={R_p3:.3f}',
             f'Var4, R={R_p4:.3f}'])

print("\n\nЗадания 2 и 3. Апроксимация : ", "\nX:", X, "\nY:", Y, "\n\nA_var1:", A_k, "\nA_var2:", A_k2, "\nA_var3:", A_k3, "\nA_var4:", A_k4, "\n\nR_var1:", R_p, "\nR_var2:", R_p2, "\nR_var3:", R_p3, "\nR_var4:", R_p4)

#plot.show()
plot.savefig("graphs/approximation.jpg")
plot.close("all")

# Nonlinear system
# Задание 4

def f(x):
    f1 = (x[0]**2)/5 + (x[1]**2)/5 - x[0]*x[1]
    f2 = np.sin(x[0]) + np.cos(x[1]) - 0.5
    return np.array([f1,f2])

def J(x):
    df1_dx1 = (2*x[0])/5 - x[1]
    df1_dx2 = (2*x[1])/5 - x[0]
    df2_dx1 = np.cos(x[0]) 
    df2_dx2 = -1 * np.sin(x[1])
    return np.array([[df1_dx1, df1_dx2],
                    [df2_dx1, df2_dx2]])
e = 0.001
xzero = np.array([0, 1])
xres = tools2_test.newton_rafson(f, J, xzero, e)

print(f"\nЗадание 4. Решение СНУ : \n[x, y] = [{xres[0]:.6f}, {xres[1]:.6f}] \n[f1, f2] = [{f(xres)[0]:.6f}, {f(xres)[1]:.6f}]")

# 3D graphs and local MIN/MAX in 3D
# Задание 5аб

def f(x):
    return (-1*(1 + np.cos(12*np.sqrt(x[0]**2 + x[1]**2))) \
            /(0.5 * (x[0]**2 + x[1]**2) + 2))

x1_rule = np.linspace(-5, 5, 101) # in interval -5 to 5 with 101 values 
x2_rule = np.linspace(-5, 5, 101)
x1,x2 = np.meshgrid(x1_rule, x2_rule) # just two linspaces wont work we need to interate througt all ys with all xs
X = [x1, x2]
Y = f(X)

ax1 = plot.subplot(1, 2, 2, projection='3d') # график
ax2 = plot.subplot(1, 2, 1) # линии уровня

ax1.plot_surface(x1, x2, Y, cmap='plasma')
ax2.contour(x1, x2, Y, levels=15)

h = 1
e = 0.001

xmins = []
xzs = [[2,2],[2,-2],[-2,2],[-2,-2]]
xmins = []
for i, xz in enumerate(xzs):
    xmins.append(tools2_test.simplex(f, xz, h, e))

    ax2.plot(xmins[i][0], xmins[i][1],'r*')

plot.title("Задание 5")
#plot.show()
plot.savefig("graphs/MINS.jpg")
plot.close('all') # remove old graphs

