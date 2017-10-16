"""
Convert decimal number to binary
"""
def reverse(l):
    l2 = []
    for i in range(len(l)):
        l2.append(l[len(l)-(i+1)])
    return l2        

def binary(n):
    i = 0
    l = []
    k = n
    while 2**i <= n:
        if k % 2 == 0:
            l.append('0')
            k /= 2
        else:
            l.append('1')
            k -= 1
            k /= 2
        i += 1
    l2 = reverse(l)
    string = ''.join(l2)
    return string

def shell():
    print ("Enter the number you wish to find the binary form of or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("Please enter an integer greater than or equal to 1")
        else:
            print(binary(int(entry)))

shell() 
