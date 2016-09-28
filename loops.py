def power(b,p):
    result=1
    for x in range(p):
       result*=b
        #result=result*b
    return result

print power(2,4)



# python 2

def summedOdds( L ):
    """ loop-based function to return a numeric list, summed
        (sum is built-in, so we're using a different name)
        input: L, a list of integers
        output: the sum of the list L
    """
    result = 0
    for element in L:
        if element %2 ==1: #checking if the current elemnt is odd
            result = result + element  # if it is odd, add it to the result, or result += e
    return result

# tests!
print "summedOdds( [4,5,6] ): should be 5 == ", summedOdds( [4,5,6] )
print "summedOdds( range(3,10) ): should be ?== ", summedOdds( range(3,10) )

import time

def mult(m,n):
    result = 0
    if m==0 or n==0:
        return 0
    elif n>0:
        for i in range(n):
            result = result+m
            #print result
            #time.sleep(2)
        return result
    elif n<0:
        for i in range(-1*n):
            result = result+m
        return -1*result
print "mult(6,7)    42 ==", mult(6,7)
print "mult(6,-7)  -42 ==", mult(6,-7)
print "mult(-6,7)  -42 ==", mult(-6,7)
print "mult(-6,-7)  42 ==", mult(-6,-7)
print "mult(6,0)     0 ==", mult(6,0)
print "mult(0,7)     0 ==", mult(0,7)
print "mult(0,0)     0 ==", mult(0,0)



def count_evens(L):
    n = 0
    for x in L:
        if x%2 == 0:
            n = n+1
    return n

print "count_evens([2, 1, 2, 3, 4], 3 == ", count_evens([2, 1, 2, 3, 4])
print "count_evens([2, 2, 0]), 3 == ", count_evens([2, 2, 0])
print "count_evens([1, 3, 5]), 0 == ", count_evens([1, 3, 5])

def dot(L,K):
    result = 0
    for i in range(len(L)):
        if len(L) == len(K):
            result = result + L[i]*K[i]
    return result

print "dot( [5,3], [6,4] )     42.0 ==", dot([5,3],[6,4])
print "dot( [1,2,3,4], [10,100,1000,10000] )  43210.0 ==", dot( [1,2,3,4], [10,100,1000,10000] )
print "dot( [5,3], [6] )        0.0 ==", dot( [5,3], [6] )
print "dot( [], [6] )           0.0 ==", dot( [], [6] )
print "dot( [], [] )            0.0 ==", dot( [], [] )



def count9(L):
    result = 0
    for x in L:
        if L[x] == 9:
            result = result + 1
    return result
print "count9([1, 2, 9]), 1 == ",count9([1, 2, 9])
print "count9([1, 9, 9]), 2 == ",count9([1, 9, 9])
print "count9([1, 9, 9, 3, 9]), 3 == ",count9([1, 9, 9, 3, 9])
