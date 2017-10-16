"""
Perform bubble sort on a list of integers.
Bubble sort, sometimes referred to as sinking sort, is a simple sorting
algorithm that repeatedly steps through the list to be sorted, compares each
pair of adjacent items and swaps them if they are in the wrong order. The
pass through the list is repeated until no swaps are needed, which indicates
that the list is sorted.
"""

def bubble_run(l):
    lold = l
    changed = 1
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
        else:
            pass
    if lold == l:
        changed = 0
    return l

def bubble(l):
    changed = 1
    lold = []
    while True:
        for a in l:
            lold.append(a)
        changed = 1
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
            else:
                pass
        if lold == l:
            break
        else:
            lold = []
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
            print(l)
            print(bubble(l))
        except NameError:
            print("Please enter a list of numbers, in the form 2,3,4,5.")
            

shell()

