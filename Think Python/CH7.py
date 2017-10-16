import math
pi = math.pi

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



def srinivasa():
    epsilon = 1
    i = 0
    est_inv = 0
    a = 2*(2**0.5)/9801
    while epsilon > 10e-15:
        b = factorial(4*i)*(1103+26390*i)
        c = factorial(i)*(396**(4*i))
        est_inv += (a*b)/c
        est = 1/est_inv
        epsilon = abs(pi - est)
        i += 1
    return est

print(srinivasa())
