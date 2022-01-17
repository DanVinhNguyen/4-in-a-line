# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:40:41 2022

@author: Dan
"""
import copy
import time
import math

class Board:
    def __init__(self, matrix = None):
        if matrix is None:
            self.matrix = [[None for i in range(8)] for i in range(8)]
        else:
            self.matrix = matrix

        self.evaluation = evaluateBoardState(self.matrix, "X") - evaluateBoardState(self.matrix, "O")
        
        self.moveOrder = []

    def getMoveOrder(self):
        return self.moveOrder
    
    def setMoveOrder(self, order):
        self.moveOrder = order

    def resetMoveOrder(self):
        self.moveOrder = []
        
    def appendMove(self, move):
        self.moveOrder.append(move)

    # this is what determines the best fit move on the board.
    def getFirstMove(self):
        return self.moveOrder[0]

    def printMatrix(self):
        matrix = self.matrix
        n = len(matrix)
        
        print("  1 2 3 4 5 6 7 8")
        for row in range(n):
            for col in range(n):
                if col == 0:
                    print(f"{chr(65 + row)}", end = " ")
                if matrix[row][col] == None:
                    print("_", end = " ")
                elif matrix[row][col] == "X":
                    print("X", end = " ")
                elif matrix[row][col] == "O":
                    print("O", end = " ")
            print()
        print()
        
    def printActual(self):
        matrix = self.matrix
        n = len(matrix)
        
        for row in range(n):
            for col in range(n):
                if matrix[row][col] is None:
                    print("_", end = ' ')
                else:
                    print(f"{matrix[row][col]}", end = ' ')
            print()
        print()
        
        
# utility to help process elements in the alpha-beta recursive calling
class Utility_function:
    def __init__(self, evaluation):
        self.evaluation = evaluation


# alpha beta search algorithm
def alpha_beta_search(board, userKey):
    # sets the time of termination
    terminalTime = time.time_ns() + 5000000000
    
    # utility functions for placeholders (used for obj.evaluation checking)
    alpha = Utility_function(-math.inf)
    beta = Utility_function(math.inf)
    
    # resets the move order as to preserve the first move.
    board.resetMoveOrder()
    
    # actual algorithm
    boardDescision = max_value(board.matrix, alpha, beta, userKey, terminalTime)
    
    return boardDescision


# half of the recursive calls
def max_value(board, alpha, beta, userKey, terminalTime):
    # check for terminal condition (time passed (5 seconds))
    if time.time_ns() >= terminalTime and isSolved(board) == False:
        return board
    
    # set the utility holder to negative infinity
    v = Utility_function(-math.inf)
    
    # generate successors
    successors = generateChildren_v2(board, oppositeKey(userKey))
    
    # process all board states and find the max value
    for obj in successors:
        v = max_evaluation(v, min_value(obj, alpha, beta, oppositeKey(userKey), terminalTime))
        
        if v.evaluation >= beta.evaluation:
            return v
        
        alpha = max_evaluation(alpha, v)
    return v


# the other half of the recursive calling
def min_value(board, alpha, beta, userKey, terminalTime):
    # check for terminal condition (time passed (5 seconds))
    if time.time_ns() >= terminalTime and isSolved(board) == False:
        return board
    
    # set the utility holder to positive infinity
    v = Utility_function(math.inf)
    
    #generate successors
    successors = generateChildren_v2(board, oppositeKey(userKey))
    
    for obj in successors:
        v = min_evaluation(v, max_value(obj.matrix, alpha, beta, oppositeKey(userKey), terminalTime))
    
        if v.evaluation <= alpha.evaluation:
            return v
        
        beta = min_evaluation(beta, v)
    return v


# returns the object with higher evaluation
def max_evaluation(obj1, obj2):
    if obj1.evaluation >= obj2.evaluation:
        return obj1
    else:
        return obj2
    

# returns the object with lower evaluation
def min_evaluation(obj1, obj2):
    if obj1.evaluation <= obj2.evaluation:
        return obj1
    else:
        return obj2


# returns the opposite userKey than the one entered. Helps with unifiying and genericizing
def oppositeKey(userKey):
    if userKey == "X":
        return "O"
    else:
        return "X"
    
# checks the board state to see if it has a solved solution
def isSolved(board):
    # There is a buffer of 1,000,000 in the evaluation score to acount for all possible combinations
    if (board.evaluation >= 90000000) or (board.evaluation <= -90000000):
        return True
    return False


# this function counts the original value in it's calculation
def evaluateBoardState(matrix, userKey):
    evaluationTotal = 0

    # parse through the entire matrix and look for the userKey (either O or X)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            
            # prioritize winning
            winCondition = 0
            # search for win condition on row
            
            # checks column for win
            if inBounds(matrix, row + 3, col):
                for i in range(4):
                    if matrix[row + i][col] == userKey:
                        winCondition += 1
                    else:
                        winCondition = 0
                        break
                    
            # if the win condition is met, set the evaluation total to a really high number
            if winCondition == 4:
                evaluationTotal += 100000000
            
            # checks row for win
            if inBounds(matrix, row, col + 3):
                # search for win condition on column
                for i in range(4):
                    if matrix[row][col + i] == userKey:
                        winCondition += 1
                    else:
                        winCondition = 0
                        break
            
            # if the win condition is met, set the evaluation total to a really high number
            if winCondition == 4:
                evaluationTotal += 100000000
            
            
            # check for the selected key (either O or X)
            if matrix[row][col] == userKey:
                ''' up '''
                evaluationTotal = evaluateDirection(matrix, row, col, userKey, -1, 0, evaluationTotal)
                    
                ''' down '''
                evaluationTotal = evaluateDirection(matrix, row, col, userKey, 1, 0, evaluationTotal)
                    
                ''' right '''
                evaluationTotal = evaluateDirection(matrix, row, col, userKey, 0, 1, evaluationTotal)
                    
                ''' left '''
                evaluationTotal = evaluateDirection(matrix, row, col, userKey, 0, -1, evaluationTotal)
                
    #print(f"{evaluationTotal = }")
    return evaluationTotal


# updates currentTotal with a specific direction
def evaluateDirection(matrix, row, col, userKey, rowMulti, colMulti, currentTotal):
    temp = 0
    
    # check for index out of bounds
    if inBounds(matrix, row + (3 * rowMulti), col + (3 * colMulti)):
        
        # check if the matrix values are valid
        for i in range(1, 4):
            if matrix[row + (i * rowMulti)][col + (i * colMulti)] == userKey:
                # check how userKeys are in the row and add to temp
                temp += 5
            elif matrix[row + (i * rowMulti)][col + (i * colMulti)] is None:
                temp += 1
            else:
                temp = 0
                break
        currentTotal += temp
        
    return currentTotal


# this function generates children around the already inserted inputs
def generateChildren_v1(board, userKey):
    matrix = board.matrix
    charList = ["X", "O"]
    n = len(matrix)
    childrenList = []
    
    # iterate through the entire matrix
    for row in range(n):
        for col in range(n):
            # search for either X or O to generate children off of
            if matrix[row][col] in charList:
                # generate the children around inputs
                ''' up '''
                childrenList = generateChild(matrix, row - 1, col, userKey, childrenList)
                
                ''' down '''
                childrenList = generateChild(matrix, row + 1, col, userKey, childrenList)
                    
                ''' right '''
                childrenList = generateChild(matrix, row, col + 1, userKey, childrenList)
    
                ''' left '''
                childrenList = generateChild(matrix, row, col - 1, userKey, childrenList)
    
    return childrenList


# this function generates children for every single available space
def generateChildren_v2(board, userKey):
    matrix = board.matrix
    n = len(matrix)
    childrenList = []
    
    # iterate through the entire matrix
    for row in range(n):
        for col in range(n):
                childrenList = generateChild(board, row, col, userKey, childrenList)
            
    return childrenList


# generates one children in a specific cardinal direction
def generateChild(parent, row, col, userKey, childrenList):
    # check if there is a bounds error, or value already placed in slot
    if isSafe(parent.matrix, row, col):
        tempParent = copy.deepcopy(parent.matrix)
        
        # set the matrix as the userKey (either O or X)
        tempParent[row][col] = userKey
        
        # create a new child node
        child = Board(tempParent)
        
        # copies over the move order to the parent
        child.setMoveOrder(parent.getMoveOrder())
        # appends the current move to the move order
        child.appendMove((row, col))
        
        # finally, appends the child to the childrenList
        childrenList.append(child)
        
    return childrenList


# function that checks if the coordinates are within the matrix
def inBounds(matrix, row, col):
    # we assume that matrix is an n x n matrix
    n = len(matrix)
    if row >= n or row < 0 or col >= n or col < 0:
        return False
    return True


# function checks if the spot is both in bounds and is not pre-populated
def isSafe(matrix, row, col):
    n = len(matrix)
    
    # bounds check
    if row < 0 or row >= n or col < 0 or col >= n:
        #print("Bounds error")
        return False
    
    # value check
    if matrix[row][col] != None:
        #print("value error")
        return False
    
    return True


def printMatrix(matrix):
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
    n = len(matrix)
    
    print("  1 2 3 4 5 6 7 8")
    for row in range(n):
        for col in range(n):
            if col == 0:
                print(f"{alphabet[row]}", end = " ")

            if matrix[row][col] == None:
                print("_", end = " ")
            elif matrix[row][col] == "X":
                print("X", end = " ")
            elif matrix[row][col] == "O":
                print("O", end = " ")
            elif matrix[row][col] == "W":
                print("W", end = " ")
        print()
    print()


if __name__ == "__main__":
    
    blank =[[None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None,  "X", None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]
    
    test = [[None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None,  "X", None, None, None, None, None],
            [None, None, None, None,  "O", None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]]
    
    #evaluationTotal = test1(computer) - test2(user)
    
    #printMatrix(blank)
    
    child = generateChildren_v2(blank, "O")

    child[0].printMatrix()
