def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

#print fib(50)


def fibIter(n):
    fibSeq = [0,1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,n):
            fibSeq.append(fibSeq[i-1]+fibSeq[i-2])
            #print fibSeq
        return fibSeq[-1]

#print fibIter(90)


def listReverse(L):
    if len(L) == 1:
        return L
    else:
        return L(-1) + listReverse(L[0:1]) or listReverse(L[1:])+(L[0])


def listReverseIter(L):
    K = []
    for i in range(len(L)-1,-1,-1) or range(-1,-1*len(L),-1):
        K.append(L[i])
    return K
# List Reverse Tests

#print listReverse(1,2,3,4,5)
#print listReverse(5,4,3,2,1)
