def bisect(f,a,b,e):
    c = (a+b)/2
    while abs(f(c)) > e:
        if f(a)*f(c) > 0:
            a = c
        else:
            b = c
        c = (a+b)/2
    return c

def newton(f,x,e):
    while abs(f(x)) > e:
        x = x - (e*f(x)/(f(x+e)-f(x)))
    return x
