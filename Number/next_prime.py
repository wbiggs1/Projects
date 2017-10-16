"""
Find the next prime number after a number n. The code is based on factorising.py
so is not as fast as it could be.
"""
   
from factorising import factorise

def next_prime(n):
    k = n+1
    while True:
        if len(factorise(k)) == 1:
            break
        else:
            k += 1
    return k

"""
Adapt factorising code to streamline.
"""
def seek_factor(n): #This outputs a factor of n if n is not prime, or an empty list if it is prime
    import math
    l = []
    if n == 1:
        l = [1]
    elif n == 2:
        pass
    elif n % 2 == 0 and n != 2:
        l.append(2)
    else:
        m = math.ceil(math.sqrt(n))
        while m < (n+1)/2:
            q = m**2 - n
            """ If q is square, say r = sqrt(q), then n = m**2 - r**2, so that
             n = (m+r)(m-r)
            """
            if q == int(math.sqrt(q))**2:
                l.append(int(m + math.sqrt(q)))
                break
            else:
                m += 1
    return l

def next_prime2(k):
    import math
    n = k+1
    while True:
        if seek_factor(n) == []:
            break
        else:
            n += 1
    return n


def is_prime(n):
    if seek_factor(n) == []:
        return True
    else:
        return False

def next_prime3(k):
    n = k+1
    while True:
        if is_prime(n):
            break
        else:
            n += 1
    return n


def shell():
    print ("Enter the number you wish to find the next prime above or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Please enter an integer greater than or equal to 1")
        else:
            print(next_prime3(int(entry)))

shell()
