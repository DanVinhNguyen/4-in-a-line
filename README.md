# 4-in-a-line
This program utilizes the alpha-beta pruning version of the mini-max algorithm to play a game of 4-in-a-line with the player.

## Mini-Max Algorithm: 
The mini-max algorithm assumes that each player will choose the action that maximizes their chance to win, and the opponent will choose the action that will minimize their opponents chances of winning.

## Alpha-Beta Pruning
This is an artificial intelligence search algorithm that seeks to reduced the number of nodes that are evaluated in the minimax algorithm search tree.

## Approach:
To start the project I took a class-based approach, where I would generate a board state and input it into a class. This class would then calculate the evaluation of the board, which utilized a weighted approach to determine if there was enough space for a win condition to exist.

## Approach to Weight Based System
I chose to calculate the evaluation by several steps, the first was if there were any winning conditions in the tree, “4 in a row’s” or “4 in a column”, this condition was given a weight of 1,000,000 as to prioritize this over everything else. The next step that I took was validating if there was enough space for a win condition to exist, this was done by first checking if a specific coordinate had an “X”, then it searched the three squares in the four directions: up, down, left, and right. If the path had no blocks (either an opponent symbol in the way, or enough space to not go out of bounds), the evaluation function would then award 5 points for each “X” in the direction (not counting the original “X”) and 1 point for each empty space otherwise if there was not enough space for a winning condition then no points would be awarded for all the counted spaces. This was then calculated separately for the “O” input and was then the difference between the ‘X’ evaluation minus ‘O’ evaluation.

## How the Algorithm Determines What Squares To Check
This first approach that I took was to check every single empty square and generate new children for every single empty square, this however, is very inefficient. A much better approach is to generate children for the adjacent squares next to the existing inputs, this has the benefit of more likely to be a possible "win" or blocking the opponent's "win" and also decreasing the possible pool of searches for the algorithm to run. This second approach however does have it's pitfalls, where the algorithm cannot predict if the player inputs random tiles not adjacent to any other inputs.
