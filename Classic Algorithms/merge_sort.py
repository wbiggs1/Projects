"""
Merge sort
"""

def divide(l):
    n = int(len(l)/2)
    l1 = []
    l2 = []
    for i in range(len(l)):
        if i < n:
            l1.append(l[i])
        else:
            l2.append(l[i])
    return (l1, l2)

def combine(l1,l2):
    l = []
    while len(l1) > 0 or len(l2) > 0:
        if len(l1) > 0 and len(l2) > 0:
            if l1[0] < l2[0]:
                l.append(l1[0])
                l1.remove(l1[0])
            else:
                l.append(l2[0])
                l2.remove(l2[0])
        elif len(l1) == 0:
            l.append(l2[0])
            l2.remove(l2[0])
        elif len(l2) == 0:
            l.append(l1[0])
            l1.remove(l1[0])
    return l

def merge(l):
    if len(l) <= 1:
        pass
    else:
        l1, l2 = divide(l)
        l1, l2 = merge(l1), merge(l2)
        l = combine(l1, l2)
    return l


def shell():
    print ("Enter the list, in the form 1,2,3,4, that you wish to sort or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        l = entry.split(',')
        if entry == "quit":
            break
        try:
            for i in range(len(l)):
                l[i] = float(l[i])
                if l[i] % 1 == 0:
                    l[i] = int(l[i])
            print(merge(l))
        except NameError:
            print("Please enter a list of numbers, in the form 2,3,4,5.")
            

shell()
        
    

