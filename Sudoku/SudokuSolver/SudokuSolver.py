'''
Created on 19.09.2011

@author: Marcus Kesper, FFHS

Brute force method to solve Sudokus
'''

import copy

def initialize():
    sudoku = [[0] * 9 for i in range(9)]
    return sudoku
    
def initAssignment():
    assignment = [[0] * 9 for i in range(9)]

    for i in range(9):
        for j in range(9):
            assignment[i][j] = [1,2,3,4,5,6,7,8,9]
    return assignment

def startAssignment(sudoku, assignment):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                assignment[i][j] = []
    return assignment

def redoAssignment(sudoku, assignment):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                for k in range(9):
                    if assignment[i][k].__contains__(sudoku[i][j]):
                        assignment[i][k].remove(sudoku[i][j])
                    if assignment[k][j].__contains__(sudoku[i][j]):
                        assignment[k][j].remove(sudoku[i][j])
                for k in range(i/3*3,i/3*3+3):
                    for l in range(j/3*3,j/3*3+3):
                        if assignment[k][l].__contains__(sudoku[i][j]):
                            assignment[k][l].remove(sudoku[i][j])
    return assignment

# to define the starting point
def startState(sudoku):
    sudoku[0][1] = 5
    sudoku[0][3] = 6
    sudoku[0][5] = 4
    sudoku[0][7] = 9
    sudoku[1][0] = 6
    sudoku[1][4] = 2
    sudoku[1][8] = 3
    sudoku[2][4] = 7
    sudoku[3][0] = 4
    sudoku[3][8] = 7
    sudoku[4][1] = 9
    sudoku[4][2] = 8
    sudoku[4][4] = 6
    sudoku[4][6] = 5
    sudoku[4][7] = 1
    sudoku[5][0] = 2
    sudoku[5][8] = 8
    sudoku[6][4] = 3
    sudoku[7][0] = 9
    sudoku[7][4] = 1
    sudoku[7][8] = 2
    sudoku[8][1] = 1
    sudoku[8][3] = 9
    sudoku[8][5] = 5
    sudoku[8][7] = 7
    return sudoku

def showSquare(sudoku):
    for i in range(9):
        print i,': ',
        for j in range(9):
            print sudoku[i][j],
        print ''

def fillSudoku(sudoku, assignment):
    global nrIt
    nrIt = nrIt + 1
    
    if isComplete(sudoku):
        return sudoku

    min = 10
    
    for i in range(9):
        for j in range(9):
            if assignment[i][j].__len__() < min and assignment[i][j].__len__() > 0  and sudoku[i][j] == 0:
                min = assignment[i][j].__len__()
                minI = i
                minJ = j

    if min == 10:
        return 0            

    if min < 10:

        oldSudoku = copy.deepcopy(sudoku)
        oldAssignment = copy.deepcopy(assignment)
        valuestoTry = copy.deepcopy(assignment[minI][minJ])
        for valuetoTry in valuestoTry:
            sudoku[minI][minJ] = valuetoTry
            assignment[minI][minJ].remove(valuetoTry)
            assignment = redoAssignment(sudoku, assignment)
            sodukoN = fillSudoku(sudoku, assignment)
            if sodukoN != 0:
                return sodukoN
            else:
                sudoku = copy.deepcopy(oldSudoku)
                assignment = copy.deepcopy(oldAssignment)
    return 0
  
def isComplete(sudoku):
    for i in range(9):
        for j in range(9):                      
            if (sudoku[i][j] == 0):
                    return 0
    return 1

def showAssignment(assignment):
    for i in range(9):
        for j in range(9):
            print(i,j,assignment[i][j])

print('Initialisierung.....')
nrIt = 0
mySudoku = initialize()
myAssignment = initAssignment()

print('Definiere Startzustand.....')
myStartSudoku = startState(mySudoku)
showSquare(myStartSudoku)
startAssignment = startAssignment(myStartSudoku, myAssignment)
newAssignment = redoAssignment(myStartSudoku, startAssignment)

print('Suche Loesung.....')
myEndSudoku = fillSudoku(myStartSudoku, newAssignment)

if isComplete(myEndSudoku):
    print '..... fertig'
    print 'Anzahl Iterationen: ',nrIt
    showSquare(myEndSudoku)
else:
    print 'kein Sudoku gefunden'
    showSquare(myEndSudoku)
