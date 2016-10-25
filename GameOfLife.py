# python 2
#
# Game of Life
#
# Name: Frank
#

import random

def createOneRow(width):
    """ returns one row of zeros of width "width"...
         You should use this in your
         createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row
#print createOneRow(5)

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A.append(createOneRow(width))
    return A
def printBoard(A):
    for row in A:
        line = ''
        for col in row:
            line += str(col)
        print line
def diagonalize(width, height):
    """ creates an empty board and then modifies it
        so that it has a diagonal strip of "on" cells.
    """
    A = createBoard(width, height)

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A
def innerCells(w,h):
    '''
    creates an empty board and modifies it so all but the boarders are on
    '''
    A = createBoard(w,h)
    for row in range(h):
        if row == 0 or row == h-1:
            for col in range(w):
                A[row][col] = 0
        else:
            for col in range(w):
                if col == 0 or col == w-1:
                    A[row][col] = 0
                else:
                    A[row][col] = 1
    return A

def randomCells(w,h):
    '''
    creates an empty board and modifies it so all boarders are off, and all inners are randomly either on or off
    '''
    A = createBoard(w,h)
    for row in range(h):
        if row == 0 or row == h-1:
            for col in range(w):
                A[row][col] = 0
        else:
            for col in range(w):
                if col == 0 or col == w-1:
                    A[row][col] = 0
                else:
                    A[row][col] = random.choice([0,1])
    return A
