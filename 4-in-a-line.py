# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:40:41 2022

@author: Dan
"""

class Game:
    
    def __init__(self):
        self.matrix = [[None for i in range(8)] for i in range(8)]



def printMatrix(matrix):
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
    n = len(matrix)
    
    print("  1 2 3 4 5 6 7 8")
    for i in range(n):
        for j in range(n):
            if j == 0:
                print(f"{alphabet[i]}", end = " ")
                if matrix[i][j] == None:
                    print("_", end = " ")
                elif matrix[i][j] == "X":
                    print("X", end = " ")
                elif matrix[i][j] == "O":
                    print("O", end = " ")
            else:
                if matrix[i][j] == None:
                    print("_", end = " ")
                elif matrix[i][j] == "X":
                    print("X", end = " ")
                elif matrix[i][j] == "O":
                    print("O", end = " ")
        print()
    print()
    
def evaluateBoardState():
    pass

    something = 0

    # check for if the opponent is going to win, and prioritize that over anything else
    
    
    
    return something


def validMoves(matrix, row, col):
    pass

    '''
    Check up first
    '''
    # check for bounds first
    


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
    
    printMatrix(test)