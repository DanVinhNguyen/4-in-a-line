# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:40:41 2022

@author: Dan
"""
import copy


class Board:
    
    def __init__(self, matrix = None):
        
        if matrix is None:
            self.matrix = [[None for i in range(8)] for i in range(8)]
        else:
            self.matrix = matrix

        self.evaluation = evaluateBoardState(self.matrix, "X") - evaluateBoardState(self.matrix, "O")
        
    def printMatrix(self):
        matrix = self.matrix
        
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
            
            # checks row for win
            if inBounds(matrix, row, col + 4):
                # search for win condition on column
                for i in range(4):
                    if matrix[row][col + i] == userKey:
                        winCondition += 1
                    else:
                        winCondition = 0
                        break
            
            # if the win condition is met, set the evaluation total to a really high number
            if winCondition == 4:
                evaluationTotal = 1000000
            
            
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


def inBounds(matrix, row, col):
    # we assume that matrix is an n x n matrix
    n = len(matrix)
    
    if row >= n or row < 0 or col >= n or col < 0:
        return False
    
    return True


# this function generates children around the already inserted inputs
def generateChildren(matrix, userKey):
    charList = ["X", "O"]
    n = len(matrix)
    childrenList = []
    
    # copy the original matrix
    parent = copy.deepcopy(matrix)
    
    # iterate through the entire matrix
    for row in range(n):
        for col in range(n):
            # search for either X or O to generate children off of
            if matrix[row][col] in charList:
                #import pdb; pdb.set_trace()
                # generate the children around inputs
                ''' up '''
                child = generateChild(parent, row - 1, col, userKey)
                if child is not None:
                    childrenList.append(child)
                
                ''' down '''
                child = generateChild(parent, row + 1, col, userKey)
                if child is not None:
                    childrenList.append(child)
                    
                ''' right '''
                child = generateChild(parent, row, col + 1, userKey)
                if child is not None:
                    childrenList.append(child)
    
                ''' left '''
                child = generateChild(parent, row, col - 1, userKey)
                if child is not None:
                    childrenList.append(child)
    
    return childrenList


def generateChild(parent, row, col, userKey):
    child = None
    
    if isSafe(parent, row, col):
        # set the matrix as the userKey (either O or X)
        parent[row][col] = userKey
        # create a new child node
        child = Board(parent)
        
        # undo the change
        parent[row][col] = None
        
    return child


# function checks if the spot is both in bounds and is not pre-populated
def isSafe(matrix, row, col):
    n = len(matrix)
    
    # bounds check
    if row < 0 or row >= n or col < 0 or col >= n:
        print("Bounds error")
        return False
    
    # value check
    if matrix[row][col] != None:
        print("value error")
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
    
    child = generateChildren(blank, "X")
    
    print(child)
    
    for i in child:
        i.printMatrix()
