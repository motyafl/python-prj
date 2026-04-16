import numpy as np
def lagrange(x, X, Y):
    S = 0
    n = len(X)
    for i in range(n):
        P = Y[i]
        for j in range(n):
            if i != j :
                P = P*((x-X[j]) / (X[i]-X[j]))
        S = S+P
    y = S
    return y

def approximate_kr(x, y):
    n = len(x)
    x = x.reshape((n, 1)) # reshape array to horizontal
    y = y.reshape((n, 1)) # reshape array to horizontal
    fi = np.ones((n, 1)) # array of once

    fi = np.hstack([fi, x, x**2, np.exp(x), np.exp(-x)]) # glue arrays together horizontally
    fit = fi.T # transpond matrix
    n = np.dot(fit, fi)
    b = np.dot(fit, y)
    a = np.linalg.solve(n, b)
    return a

def approximate_kr2(x, y):
    n = len(x)
    x = x.reshape((n, 1)) # reshape array to horizontal
    y = y.reshape((n, 1)) # reshape array to horizontal
    fi = np.ones((n, 1)) # array of once

    fi = np.hstack([fi, x, x**2, np.sin(x), np.cos(x)]) # glue arrays together horizontally
    fit = fi.T # transpond matrix
    n = np.dot(fit, fi)
    b = np.dot(fit, y)
    a = np.linalg.solve(n, b)
    return a


def approximate_kr3(x, y):
    n = len(x)
    x = x.reshape((n, 1)) # reshape array to horizontal
    y = y.reshape((n, 1)) # reshape array to horizontal
    fi = np.ones((n, 1)) # array of once

    fi = np.hstack([fi, x**2, x**4, np.sin(x), np.cos(x)]) # glue arrays together horizontally
    fit = fi.T # transpond matrix
    n = np.dot(fit, fi)
    b = np.dot(fit, y)
    a = np.linalg.solve(n, b)
    return a

def approximate_kr4(x, y):
    n = len(x)
    x = x.reshape((n, 1)) # reshape array to horizontal
    y = y.reshape((n, 1)) # reshape array to horizontal
    fi = np.ones((n, 1)) # array of once

    fi = np.hstack([fi, x, x**3, x**5, np.arctan(x)]) # glue arrays together horizontally
    fit = fi.T # transpond matrix
    n = np.dot(fit, fi)
    b = np.dot(fit, y)
    a = np.linalg.solve(n, b)
    return a

def newton_rafson(f,J,x,e):
    fx = f(x)
    while np.linalg.norm(f(x)) > e: # norm is abs for vectors
        #x = x - np.linalg.inv(J(x))@fx # where @ is the same as np.dot() or a dot product
        x = x - np.linalg.solve(J(x), fx) # more effective
        fx = f(x)
    return x

def find_worst(fs):
    n=len(fs)
    i_worst=0
    for i in range(1,n):
        if fs[i]>fs[i_worst]:
            i_worst=i
    return i_worst

def find_best(fs):
    n=len(fs)
    i_best=0
    for i in range(1,n):
        if fs[i]<fs[i_best]:
            i_best=i
    return i_best


def simplex(f,x,h,e):
    x=np.array(x).reshape((1,2))
    xs=np.vstack((x, x+[h,0], x+[0,h]))
    fs=np.array([f(xs[0]),f(xs[1]),f(xs[2])])
    while True:
        i_w=find_worst(fs)
        x_w=xs[i_w]
        x_ref=sum(xs)-2*x_w
        f_ref=f(x_ref)
        if fs[i_w]>f_ref:
            xs[i_w]=x_ref
            fs[i_w]=f_ref
        else:
            i_b=find_best(fs)
            x_b=xs[i_b]
            h=h/3
            if h>e:
                x=x_b
                xs=np.vstack((x, x+[h,0], x+[0,h]))
                fs=np.array([f(xs[0]),f(xs[1]),f(xs[2])])
            else:
                return x_b
