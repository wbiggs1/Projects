# Coin toss

import random
count = 0
heads = 0
tails = 0

while count < 100:
    i = random.randint(0,1)
    if i == 1:
        heads += 1
    else:
        tails += 1
    count += 1

print("Number of heads =", heads)
print("Number of tails =", tails)
        
            
    
