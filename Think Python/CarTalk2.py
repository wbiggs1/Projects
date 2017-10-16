"""
“Recently I had a visit with my mom and we realized that the two digits that make
up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
wondered how often this has happened over the years but we got sidetracked with other
topics and we never came up with an answer.
“When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we’re lucky it would happen again in a few years, and
if we’re really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?”
"""

def check(son_age, mum_age):
    son_age = str(son_age).zfill(2)
    mum_age = str(mum_age).zfill(2)
    return son_age[0] == mum_age[1] and son_age[1] == mum_age[0]

def matches(n):
    """n and n+1 are the two possible difference in age between the son and mum"""
    son_age = 0
    mum_age = n
    count = 0
    while mum_age < 100:
        if check(son_age, mum_age) or check(son_age, mum_age + 1):
            count += 1
        son_age += 1
        mum_age += 1
    return count

match_dict = {}
for i in range(15,60):
    match_dict[i] = matches(i)

def value_to_key(val):
    vkeys = []
    for l in match_dict:
        if match_dict[l] == val:
            vkeys.append(l)
    return vkeys

possibles = value_to_key(8)

""" This gives possible differences of 17 or 18. Investigate these."""


def print_matches(n):
    """n and n+1 are the two possible difference in age between the son and mum"""
    son_age = 0
    mum_age = n
    count = 0
    while mum_age < 100:
        if check(son_age, mum_age) or check(son_age, mum_age + 1):
            count += 1
            print(son_age,mum_age)
        son_age += 1
        mum_age += 1
    return count

print_matches(17)
print('\n')
print_matches(18)

"""Ans: He's between 57 and 67"""
