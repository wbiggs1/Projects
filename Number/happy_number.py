"""
Find whether n is a happy number, and later produce a list of the first n
happy numbers.
A happy number is defined by the following process. Starting with any positive
integer, replace the number by the sum of the squares of its digits, and repeat
the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers for which this
process ends in 1 are happy numbers, while those that do not end in 1 are
unhappy numbers.
"""
def is_happy(st):
    l = [int(st)]
    if st == '1':
        return True
    else:
        while True:
            m = 0
            for i in range(len(st)):
                m += int(st[i])**2
            st = str(m)
            if m == 1:
                return True
            else:
                for i in range(len(l)):
                    if m == l[i]:
                        return False
            l.append(m)
            
def first_n_happy(n):
    i = 1
    l = []
    while len(l) < n:
        st = str(i)
        if is_happy(st):
            l.append(i)
        i += 1
    return l
            
def shell():
    print ("Enter the number of happy numbers you want or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Please enter an integer greater than or equal to 1")
        else:
            print(first_n_happy(int(entry)))

shell()
