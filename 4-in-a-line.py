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


# this function counts the original value in it's calculation
def evaluateBoardState(matrix, userKey):
    evaluationTotal = 0

    # parse through the entire matrix and look for the userKey (either O or X)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            
            # prioritize winning
            winCondition = 0
            # search for win condition on row
            for i in range(4):
                if matrix[row + i][col] == userKey:
                    winCondition += 1
                else:
                    winCondition = 0
                    break
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
                # check for index out of bounds
                if (row - 3) >= 0:
                    temp = 0
                    # check if the matrix values are ok
                    for i in range(1, 4):
                        if matrix[row - i][col] == userKey: #or matrix[row - i][col] == None:
                            # check how userKeys are in the row and add to temp
                            temp += 5
                        elif matrix[row - i][col] == None:
                            temp += 1
                        else:
                            temp = 0
                            break
                    evaluationTotal += temp
                    
                ''' down '''
                if (row + 3) < len(matrix):
                    temp = 0
                    # check if the matrix values are ok
                    for i in range(1, 4):
                        if matrix[row + i][col] == userKey: # or matrix[row + i][col] == None:
                            # check how userKeys are in the row and add to temp
                            temp += 5
                        elif matrix[row + i][col] == None:
                            temp += 1
                        else:
                            temp = 0
                            break
                    evaluationTotal += temp
                    
                ''' right '''
                if (col + 3) < len(matrix):
                    temp = 0
                    # check if matrix values are ok
                    for i in range(1, 4):
                        if matrix[row][col + i] == userKey: # or matrix[row][col + i] == None:
                            temp += 5
                        elif matrix[row][col + i] == None:
                            temp += 1
                        else:
                            temp = 0
                            break
                    evaluationTotal += temp
                    
                ''' left '''
                if (col - 3) >= 0:
                    temp = 0
                    # check if matrix values are ok
                    for i in range(1, 4):
                        if matrix[row][col - i] == userKey: # or matrix[row][col - i] == None:
                            temp += 5
                        elif matrix[row][col - i] == None:
                            temp += 1
                        else:
                            temp = 0
                            break
                    evaluationTotal += temp
                    
    print(f"Evaluation Total: {evaluationTotal}")
    return evaluationTotal


# this function generates children around the already inserted inputs
def generateChildren(matrix, userKey):
    n = len(matrix)
    childrenList = []
    
    # copy the original matrix
    parent = copy.deepcopy(matrix)
    
    # iterate through the entire matrix
    for row in n:
        for col in n:
            # search for either X or O to generate children off of
            if matrix[row][col] == "X" or matrix[row][col] == "O":
                
                # generate the children around inputs
                ''' up '''
                childCheck(parent, row - 1, col, childrenList, userKey)
                '''
                if isSafe(matrix, row - 1, col):
                    # set the matrix as the userKey (either O or X)
                    parent[row - 1][col] = userKey
                    # create a new child node
                    child = Board(parent)
                    # undo the change
                    parent[row - 1][col] = None
                    
                    # add child to children list
                    childrenList.add(child)
                '''
                
                ''' down '''
                if isSafe(matrix, row + 1, col):
                    # set the matrix as the userKey (either O or X)
                    parent[row + 1][col] = userKey
                    # create a new child node
                    child = Board(parent)
                    # undo the change
                    parent[row + 1][col] = None
                    
                    # add child to children list
                    childrenList.add(child)
                    
                ''' right '''
                if isSafe(matrix, row, col + 1):
                    # set the matrix as the userKey (either O or X)
                    parent[row][col + 1] = userKey
                    # create a new child node
                    child = Board(parent)
                    # undo the change
                    parent[row][col + 1] = None
                    
                    # add child to children list
                    childrenList.add(child)
    
                ''' left '''
                if isSafe(matrix, row, col - 1):
                    # set the matrix as the userKey (either O or X)
                    parent[row][col - 1] = userKey
                    # create a new child node
                    child = Board(parent)
                    # undo the change
                    parent[row][col - 1] = None
                    
                    # add child to children list
                    childrenList.add(child)
    
    return



def childCheck(parent, row, col, childrenList, userKey):
    if isSafe(parent, row - 1, col):
        # set the matrix as the userKey (either O or X)
        parent[row - 1][col] = userKey
        # create a new child node
        child = Board(parent)
        # undo the change
        parent[row - 1][col] = None
        
        # add child to children list
        childrenList.add(child)


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
            [None, None, None, None, None, None,  "O", None],
            [None, None, None, None, None,  "O",  "X", None],
            [None, None, None, None, None, None,  "O", None],
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
    
    
    printMatrix(blank)
    
    evaluateBoardState(blank, "X")

    evaluateBoardState_v2(blank, "X")
    
    print(isSafe(blank, 3, 8))