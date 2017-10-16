

def pi_to_n(n):
    #Use  Gregory–Leibniz series
    pi2 = 4
    i = 1
    err = 1
    while err > 10**-(n+1):
        pi2 -= 4/(4*i-1)
        pi3 = pi2 + 4/(4*i+1)
        i += 1
        err =  abs(pi3 - pi2)
        pi2 = pi3
    pi = round(pi3, n)
    print(pi)

#Try different convergent sum (This one converges far more quickly)

def pi_to_n2(n):
    from decimal import getcontext
    from decimal import Decimal
    getcontext().prec = 4*n
    #Use Nilakantha
    pi2 = Decimal(3)
    pi3 = Decimal(4)
    i = 1
    err = 1
    while err > Decimal(10**-(n)):
        a = Decimal((-1)**(i+1)*4/(2*i*(2*i+1)*(2*i+2)))
        pi2 += Decimal(a)
        i += 1
        err =  Decimal(abs(pi3 - pi2))
        pi3 = Decimal(pi2)
    pi = round(pi3, n)
    print(pi)

# Chudnovsky algorithm. n iterations gives pi to n-1 decimal points
# Factorial required

def factorial(k):
    if k == 0:
        return 1
    return k*factorial(k-1)

def getpi(n):
    m = 0
    from decimal import getcontext
    from decimal import Decimal
    inverse = 0
    for i in range(n+1):
        num = (-1)**i * factorial(6*i)*(545140134*i + 13591409)
        den = factorial(3*i) * factorial(i)**3 * (640320**3)**(i+0.5)
        inverse += 12*num/den
    pi = Decimal(1/inverse)
    return round(pi,n)
        
def shell():
    print ("Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Please enter a number")
        else:
            print(getpi(int(entry)))

shell()

"""
Comparison of methods:
They increase in speed, from first to third, however the third struggle with
values of n around 18, as den became to large. Also some issues with each method
with final few decimal points for large n > 15. I believe this is due to python
roundinf earlier than I'd hope.
"""



    
