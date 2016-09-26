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
