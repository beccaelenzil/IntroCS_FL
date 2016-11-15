import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line
def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A.append(createOneRow(width))
    return A

def randomCells(w,h,type1,type2):
    '''
    creates an empty board and modifies it so all boarders are off, and all inners are randomly either on or off
    '''
    total = (w-2)*(h-2)
    t1 = total * type1
    t2 = total * type2
    A = createBoard(w,h)
    for row in range(h):
            for col in range(w):
                    if row == 0 or row == h-1 or col == 0 or col == w-1:
                        A[row][col] = -1
                    else:
                        num = random.randint(0,total)
                        if num < t1:
                            A[row][col] = 1
                            t1 += -1
                        elif num < t1+t2:
                            A[row][col] = 2
                            t2 += -1
                        else:
                            A[row][col] = 0
                        total += -1
    return A

def countNeighboroughs(row,col,A):
    list = [0,0,0]
    list[-1] = A[row][col]
    for r in range(row-1,row+2):
        for c in range(col-1,col+2):
            if r == row and c == col or A[r][c] == -1:
                pass
            elif A[r][c] == 1:
                list[0] += 1
            elif A[r][c] == 2:
                list[1] += 1
            else:
                pass
    return list
def listempties(A):
    empties = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            if A[row][col] == 0:
                empties.append([row,col])
    return empties
def countNeighboroughsArray(A):
    neigh = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        neigh.append([])
        for col in range(w):
            if A[row][col] == -1:
                neigh[row].append(-1)
            else:
                neigh[row].append(countNeighboroughs(row,col,A))
    return neigh
def vacateList(A,thresh):
    neigh = countNeighboroughsArray(A)
    vacaters = []
    h = len(A)
    w = len(A[0])
    for row in range(h):
        for col in range(w):
            if A[row][col] == -1:
                pass
            else:
                totalnumneighboroughs = neigh[row][col][0] + neigh[row][col][1]
                mynumneighboroughs = neigh[row][col][neigh[row][col][2]-1]
                if totalnumneighboroughs > 0:
                    if float(mynumneighboroughs)/totalnumneighboroughs < thresh and A[row][col] > 0:
                        vacaters.append([row,col])
    return vacaters
def next_life_generation(A,thresh):
    empties = listempties(A)
    vacaters = vacateList(A,thresh)
    emptiescopy = empties
    vacaterscopy = vacaters
    h = len(A)
    w = len(A[0])
    changes = [[],[]]
    for i in range(len(vacaterscopy)):
        if len(emptiescopy) > 0:
            start = random.randint(0,len(vacaterscopy)-1)
            finish = random.randint(0,len(emptiescopy)-1)
            changes[0].append(vacaterscopy[start])
            changes[1].append(emptiescopy[finish])
            vacaterscopy.remove(vacaterscopy[start])
            emptiescopy.remove(emptiescopy[finish])
    newA = []
    for row in range(h):
        newA.append([])
        for col in range(w):
            if [row,col] in changes[0]:
                newA[row].append(0)
            elif [row,col] in changes[1]:
                oldvaluecoord = changes[0][changes[1].index([row,col])]
                oldvalue = A[oldvaluecoord[0]][oldvaluecoord[1]]
                newA[row].append(oldvalue)
            else:
                newA[row].append(A[row][col])
    return newA
A = randomCells(5,5,.2,.4)
B = next_life_generation(A,.45)
printBoard(A)
printBoard(B)
