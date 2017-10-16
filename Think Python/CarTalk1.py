def is_palandrome(s):
    while len(s) > 1:
        if s[0] != s[-1]:
            return False
        else:
            s = s[1:-1]
    return True

def add_zeroes(n):
    s = str(n)
    if len(s) < 6:
        i = 6 - len(s)
        s = '0'*i + s
    return s
    
def sol(start=0):
    """returns solution of following problem:
    “I was driving on the highway the other day and I happened to notice my odometer.
    Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
    miles, for example, I’d see 3-0-0-0-0-0.
    “Now, what I saw that day was very interesting. I noticed that the last 4 digits were
    palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
    palindrome, so my odometer could have read 3-1-5-4-4-5.
    “One mile later, the last 5 numbers were palindromic. For example, it could have read
    3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
    you ready for this? One mile later, all 6 were palindromic!
    “The question is, what was on the odometer when I first looked?”
    Additional variable gives different starting point
    """
    n = start
    while True:
        m = n
        s = add_zeroes(m)
        s1 = s[2:]
        if not is_palandrome(s1):
            n += 1
        else:
            m += 1
            s = add_zeroes(m)
            s2 = s[1:]
            if not is_palandrome(s2):
                n += 1
            else:
                m += 1
                s = add_zeroes(m)
                s3 = s[1:-1]
                if not is_palandrome(s3):
                    n += 1
                else:
                    m += 1
                    s = add_zeroes(m)
                    if not is_palandrome(s):
                        n += 1
                    else:
                        return (n, s1, s2, s3, s)

" Only 6 digit solutions are 198888 and 199999 "

def has_palindrome(i, start, len):
    """Returns True if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start).
    """
    s = str(i)[start:start+len]
    return s[::-1] == s
    
"""
easier:

def check(i):

return (has_palindrome(i, 2, 4)   and
        has_palindrome(i+1, 1, 5) and
        has_palindrome(i+2, 1, 4) and
        has_palindrome(i+3, 0, 6))


def check_all():
    

    i = 100000
    while i <= 999996:
        if check(i):
            print i
        i = i + 1


print 'The following are the possible odometer readings:'
check_all()
print                       
                
"""                    
                    
            
