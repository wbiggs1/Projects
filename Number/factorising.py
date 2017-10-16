"""
Prime Factorisation using Fermat's Method
"""

def factorise(n):
    import math
    l = []
    if n == 1:
        pass
    elif n % 2 == 0:
        l.append(2)
        l.extend(factorise(n/2))
    else:
        m = math.ceil(math.sqrt(n))
        while m < (n+1)/2:
            q = m**2 - n
            """ If q is square, say r = sqrt(q), then n = m**2 - r**2, so that
            n = (m+r)(m-r)
            """
            if q == int(math.sqrt(q))**2:
                l.append(int(m + math.sqrt(q)))
                l.extend(factorise(n/(m + math.sqrt(q))))
                break
            else:
                m += 1
        """If n can be factorised, we must find such a q as above, since if n = cd,
         where c and d are odd, n = ((c+d)/2)**2 - ((c-d)/2)**2
         """
        if l == []:
            l = [int(n)]
    return l


def shell():
    print ("Enter the number you wish to factorise or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Please enter an integer greater than or equal to 1")
        else:
            print(factorise(int(entry)))

# This stops from running when I import it in next_prime            
if __name__ == '__main__':
    shell()
