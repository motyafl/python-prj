def bisect(f,a,b,e):
    c = (a+b)/2
    while abs(f(c)) > e:
        if f(a)*f(c) > 0:
            a = c
        else:
            b = c
        c = (a+b)/2
    return c

def bisect_fast(f,a,b,e):
    c = (a+b)/2
    fc = f(c)
    while abs(fc) > e:
        fc = f(c)
        if f(a)*fc > 0:
            a = c
        else:
            b = c
        c = (a+b)/2
    return c

def newton(f,x,e):
    while abs(f(x)) > e:
        x = x - (e*f(x)/(f(x+e)-f(x)))
    return x

def newton_fast(f,x,e):
    fx = f(x)
    while abs(fx) > e:
        x = x - (e*fx/(f(x+e)-fx))
        fx = f(x)
    return x

def thrsect(f, a, b, e):
    while (b-a) >= e:
        c1 = a+(b-a)/3
        c2 = b-(b-a)/3 

        if f(c1) > f(c2):
            a = c1
        else:
            b = c2
    return (c1+c2)/2

def thrsect_middle(f, a, b, e):
    while (b-a) >= e:
        c1 = (a+b)/2
        c2 = c1 + e/3

        if f(c1) > f(c2):
            a = c1
        else:
            b = c2
    return (c1+c2)/2
 
def goldenR(f, a, b, e):
    while (b-a) >= e:
        c1 = b - 0.62*(b-a)
        c2 = a + 0.62*(b-a)
        F1 = f(c1)
        F2 = f(c2)

        if F1 > F2:
            a = c1
            c1 = c2
            F1 = F2

            c2 = a + 0.618*(b-a)
            F2 = f(c2)
        else:
            b = c2
            c2 = c1
            F2 = F1

            c1 = b - 0.618*(b-a)
            F1 = f(c1)
    return (c1+c2)/2

def revstep(f, x, h, e):
    while abs(h) >= e:
        xn = x + h
        if f(xn) > f(x):
            h = -h/3
        x = xn
    return x+3*h

def stepforw(f, a, b, st):
    S = 0
    n = int((b-a)/st)
    for i in range(1, n-1, 1):
        S += st*f(a+(i-1)*st)
    return S

def stepback(f, a, b, st):
    S = 0
    n = int((b-a)/st)
    for i in range(1, n-1, 1):
        S += st*f(a+i*st)
    return S

def stepfull(f, a, b, st):
    S = 0
    Q = (st*f(a)+st*f(b))/2
    n = int((b-a)/st)
    #print("fa = ", f(a))
    #print("fb = ", f(b))
    #print("Q = ", Q)
    for i in range(1, n, 1): # n or n-1 ?
        S += st*f(a+i*st)
    #print(" S = ", S)
    return S+Q

def midpoint(f, a, b, st):
    S = 0
    n = int((b-a)/st)
    for i in range(1, n+1, 1):
        S += st*f(a+i*st-st/2)
    return S
