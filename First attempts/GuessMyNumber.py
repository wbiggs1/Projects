# Guess my number game

import random
n = random.randint(1,100)

m = int(input("Pick a number between 1 and 100."))

while m != n:
    if m < n:
        print("Too small!")
        m = int(input("Try again:"))
    else:
        print("Too high!")
        m = int(input("Try again:"))

print("Congratulations! You got it, my number was", str(n))
    
