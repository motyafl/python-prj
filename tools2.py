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

def approximate_line(X, Y):
    n = len(X)
    N = np.array([[ n,      sum(X)],
                  [ sum(X), sum(X*X)]]) # matrix
    B = np.array([[ sum(Y)   ],
                  [ sum(Y*X) ]]) # matrix
    A = np.linalg.solve(N, B)
    return A

def approximate_parabol(X, Y):
    n = len(X)
    X = X.reshape((n, 1)) # reshape array to horizontal
    Y = Y.reshape((n, 1)) # reshape array to horizontal
    ONE = np.ones((n, 1)) # array of once
    #N = np.array([[ n,      sum(X)],
    #              [ sum(X), sum(X*X)]]) # matrix
    #B = np.array([[ sum(Y)   ],
    #              [ sum(Y*X) ]]) # matrix

    Fi = np.hstack([ONE, X, X*X]) # glue arrays together horizontally
    FiT = Fi.T # transpond matrix
    N = np.dot(FiT, Fi)
    B = np.dot(FiT, Y)
    A = np.linalg.solve(N, B)
    return A

def grad_method(f, fgrad, x, h, e): #revstep in 3d
    x = np.array(x)
    while abs(h) >= e:
        xn = x - h * fgrad(x)/np.linalg.norm(fgrad(x))
        if f(xn) > f(x):
            h = h/3
        xold = x
        x = xn
    return x

def easy_grad_method(f, x, h, e): #revstep in 3d
    def fgrad(x):
        dfx0 = (f([x[0]+e,x[1]]) - fx)/e
        dfx1 = (f([x[0],x[1]+e]) - fx)/e
        return np.array([dfx0,dfx1])
    x = np.array(x)
    fx = f(x)
    while abs(h) >= e:
        fg = fgrad(x)
        xn = x - h * fg/np.linalg.norm(fg)
        fnew = f(xn)
        if fnew > fx:
            h = h/3
        xold = x
        x = xn
        fx = fnew
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

def approximate_poly(X, Y, p=2):
    n = len(X)
    X = X.reshape((n, 1)) # reshape array to horizontal
    Y = Y.reshape((n, 1)) # reshape array to horizontal
    Fi = np.ones((n, 1)) # array of once

    for i in range(1,p+1):
        Fi = np.hstack([Fi, X**i]) # glue arrays together horizontally
    FiT = Fi.T # transpond matrix
    N = np.dot(FiT, Fi)
    B = np.dot(FiT, Y)
    A = np.linalg.solve(N, B)
    return A

def approximate_custom(x, y):
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
