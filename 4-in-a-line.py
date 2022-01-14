# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:40:41 2022

@author: Dan
"""

class Game:
    
    def __init__(self):
        self.matrix = [[None for i in range(8)] for i in range(8)]




# this function counts the original value in it's calculation
def evaluateBoardState(matrix, userKey):
    evaluationTotal = 0

    # check for if the opponent is going to win, and prioritize that over anything else
    
    # parse through the entire matrix and look for the userKey (either O or X)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
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


# this function doesn't count it's original value in the calculation
def evaluateBoardState_v2(matrix, userKey):
    evaluationTotal = 0

    # check for if the opponent is going to win, and prioritize that over anything else
    
    # parse through the entire matrix and look for the userKey (either O or X)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # check for the selected key (either O or X)
            if matrix[row][col] == userKey:
                ''' up '''
                # check for index out of bounds
                if (row - 3) >= 0:
                    temp = 0
                    # check if the matrix values are ok
                    for i in range(4):
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
                    for i in range(4):
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
                    for i in range(4):
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
                    for i in range(4):
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


def validMoves(matrix, userKey):
    pass
    
    
                

    '''
    Check up first
    '''
    # check for bounds first


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
            [None, None, None, None, None, None, "O", None],
            [None, None, None, None, None, "O", "X", None],
            [None, None, None, None, None, None, "O", None],
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
    
    
    printMatrix(blank)
    
    evaluateBoardState(blank, "X")

    evaluateBoardState_v2(blank, "X")