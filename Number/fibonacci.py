"""
Find Fibbonaci Sequence up to nth number
"""
def fibbonaci(n):
    if n == 0:
        l = []
    elif n == 1:
        l = [1]
    else:
        l = [1,1]
        for i in range(n-2):
            m = l[i] + l[i+1]
            l.append(m)
    return l

def shell():
    print ("Welcome to Fibbonaci Calculator. In the shell below Enter the number of terms that should be calculated or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Please enter an integer greater than or equal to 1")
        else:
            print(fibbonaci(int(entry)))

shell()
