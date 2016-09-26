def summed(L):
    result = 0
    for i in L:
        result = result + i
        #result +=2
    return result


# python 2
#
# Homework 3, Problem 1
# Loops!
#
# Name:
#

def fac(n):
    """ loop-based factorial function
        input: a nonnegative integer n
        output: the factorial of n
    """
    result = 1                 # starting value - like a base case
    for x in range(1,n+1):     # loop from 1 to n, inclusive
        result = result * x    # update the result by mult. by x
    return result              # notice this is AFTER the loop!

# tests: run by pressing the Run button above

print "fac(0): should be 1 == ", fac(0)
print "fac(5): should be 120 == ", fac(5)
