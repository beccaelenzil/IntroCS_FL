# python 2
#
# Homework 5, Problem 1
#
# Name: Frank Larkin
#
import random

def rs():
    """ rs chooses a random step and returns it
        note that a call to rs() requires parentheses
        inputs: none at all!
    """
    return random.choice([-1,1])


def rwPos(start, nsteps):
    currentPosition = start
    for i in range (0,nsteps):
        currentPosition = (currentPosition +rsl)
        print "Current position is" + str(currentPosition)
    return currentPosition
#rwpos(1,10)

def rwsteps(start,low,hi):
    currentPosition = start
    stepCount = 0

    leftSpaces = (start-low)+1
    rightSpaces = (hi-low)-start

    while currentPosition in range(low,hi):
        currentStep = rs()
        currentPosition = currentPosition + currentStep
        stepCount += 1
        if currentStep == 1:
            leftSpaces += 1
            rightSpaces -= 1
        else:
            leftSpaces -= 1
            rightSpaces += 1

        print '|' + leftSpaces*' ' + 'XX'+rightSpaces*' ' +'|'

        print stepCount
        print currentPosition
    print 'That took '+str(stepCount)+' steps'
rwsteps(5,1,100)

