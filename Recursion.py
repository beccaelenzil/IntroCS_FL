def fibSeqReec(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibSeq(x-1)+fibSeq(x-2)

#print fibSeq(50)


def fibIter(n):
    fibSeq = [0,1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2,n):
            fibSeq.append(fibSeq[i-1]+fibSeq[i-2])
            print fibSeq
        return fibSeq[-1]

print fibIter(90)
