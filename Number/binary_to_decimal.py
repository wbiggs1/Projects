"""
Convert binary number to decimal
"""
def decimal(string):
    k = len(string)
    n = 0
    for i in range(k):
        if string[i] == '1':
            n += 2**(k-(i+1))
        else:
            pass
    return n

def shell():
    print ("Enter the binary number you wish to find the decimal form of or enter quit to exit")
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        string = str(entry)
        test = 1
        for i in range(len(entry)):
            if string[i] != '0' and string[i] != '1':
                test = 0
        if test == 0:
            print("Please enter an binary integer greater than or equal to 1")
        else:
            print(decimal(entry))

shell() 
