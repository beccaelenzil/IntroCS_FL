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

    leftSpaces = low + start
    rightSpaces = hi-start
    print '|' + leftSpaces*' ' + 'XX'+rightSpaces*' ' +'|' + 'position:' + str(currentPosition)
    while currentPosition in range(low+1,hi):
        currentStep = rs()
        currentPosition = currentPosition + currentStep
        stepCount += 1

        if currentStep == 1:
            leftSpaces += 1
            rightSpaces -= 1
        else:
            leftSpaces -= 1
            rightSpaces += 1

        print '|' + leftSpaces*' ' + 'XX'+rightSpaces*' ' +'|' + 'position:' + str(currentPosition)

    print 'That took '+str(stepCount)+' steps'

#rwsteps(10,0,50)

def rwPosPlain(start, nsteps):
    currentPosition = start
    for i in range (0,nsteps):
        currentPosition = (currentPosition +rs())
        #print "Current position is" + str(currentPosition)
    return currentPosition
#rwpos(1,10)
def ave_signed_displacement(n_sims):
    currentPositionList = []
    for n in range(n_sims):
        currentPosition = rwPosPlain(0,100)
        currentPositionList.append(currentPosition)
    ave = sum(currentPositionList)/n_sims
    return ave
#calculates the average distance from the initial value each time?
def sq_signed_displacement(n_sims):
    sq_disp_list = []
    for n in range(n_sims):
        currentPosition = rwPosPlain(0,100)
        sq_disp = currentPosition**2
        sq_disp_list.append(sq_disp)

    ave = sum(sq_disp_list)/float(n_sims)
    return ave
#Squares each value in currentPositionList and recalculates the average, thus calculating how far the thing travels each time
print sq_signed_displacement(10000)
