# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:40:41 2022

@author: Dan
"""

class Game:
    
    def __init__(self):
        self.matrix = [[None for i in range(8)] for i in range(8)]




    
def evaluateBoardState(matrix, userKey):
    pass

    something = 0

    # check for if the opponent is going to win, and prioritize that over anything else
    
    # parse through the entire matrix and look for the userKey (either O or X)
    for i in len(matrix):
        for j in len(matrix[i]):
            if matrix[i][j] == userKey:
                continue
            #now we need to check for valid moves
    
    
    return something


def validMoves(matrix, userKey):
    pass
    
    
                

    '''
    Check up first
    '''
    # check for bounds first
    
    

'''
This function does a couple things:
    1. checks the bounds of the selected place
    2. checks if there are any conflicts (anything other than the indicated string & None)
    3. returns a list with the valid moves
'''
def checkBounds(matrix, row, col):
    pass

    # check up first
    
    

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
        print()
    print()


if __name__ == "__main__":
    
    blank =[[None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
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
    
    row = 0
    column = 4
    
    blank[row][column] = "X"
    
    printMatrix(blank)