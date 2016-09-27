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


artists = []

for i in [0, 1, 2]:
    next_artist = raw_input('Enter an artist that you like:')
    artists.append(next_artist)

print ('Thank you!  We will work on your recommendations now.')



def factorial(n):
    answerSoFar = 1
    for factor in range(1, n+1):
        answerSoFar = answerSoFar * factor
    return answerSoFar
print factorial(5)



def listDoubler(aList):
    doubledList = []
    for elem in aList:
# append the value 2*elem to doubledList
        doubledList.append(2*elem)
    return doubledList

print (listDoubler([20, 21, 22]))



newPref = raw_input("Please enter the name of an \
artist or band that you like: " )

while newPref != '':
    prefs.append(newPref)
    newPref = raw_input("Please enter an artist or band \
that you like, or just press enter to see recommendations: ")

print('Thanks for your input!')



def factorial(n):
    answer = 1
    while n > 0:
        answer = answer * n
        n = n-1
    return answer



numCorrect = 0

while True:      # run forever -- or at least as long as needed...
    newPref = raw_input("Please enter an artist or band that you like, \
                 or just press enter to see recommendations: ")
    if newPref:
        prefs.append(newPref)
    else:
        break

print('Thanks for your input!')



counter = 0
while counter < 10000:
    counter = counter + 1

ran in 2.6 milliseconds. The "equivalent" recursive program

def increment(value, times):
    if times <= 0:
        return value
    return increment(value + 1, times - 1)

counter = increment(0, 10000)



