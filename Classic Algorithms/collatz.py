"""
Collatz Conjecture - Start with a number n > 1. Find the number of steps it
takes to reach one using the following process: If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
The conjecture is that this always reaches 1, for any starting point.
"""
l = []

def Collatz(n):
    l.append(int(n))
    if n == 1:
        return 0
    elif n % 2 == 0:
        n /= 2
        m = 1 + Collatz(n)
        return m
    else:
        n *= 3
        n += 1
        m = 1 + Collatz(n)
        return m

def shell():
    print ("Enter the number you wish to apply the process to or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Please enter an integer greater than or equal to 1")
        else:
            print(Collatz(int(entry)))
            print(l)

shell()
