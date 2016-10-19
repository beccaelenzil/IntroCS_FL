def rwPos(start, nsteps):
    currentPosition = start
    for i in range (0,nsteps):
        currentPosition = (currentPosition +rsl)
        print "Current position is" + str(currentPosition)
    return currentPosition


