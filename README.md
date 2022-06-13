# 4-in-a-line
This program utilizing alpha-beta pruning to play a game of 4-in-a-line with the player.

# Mini-Max Algorithm: 

# Alpha-Beta Pruning
This is an artificial intelligence search algorithm that seeks to reduced the number of nodes that are evaluated in the minimax algorithm in its search tree.

# Approach:
	To start the project I took a class-based approach, where I would generate a board state and input it into a class. This class would then calculate the evaluation of the board, which utilized a weighted approach to determine if there was enough space for a win condition to exist.

# Evaluation:
	I chose to calculate the evaluation by several steps, the first thing I validated was if there were any winning conditions in the tree, “4 in a row’s” or “4 in a column”, this condition was given a weight of 1,000,000 as to prioritize this over everything else. The next step that I took was validating if there was enough space for a win condition to exist, this was done by first checking if a specific coordinate had an “X”, then it searched the three squares in the four directions: up, down, left, and right. If the path had no blocks (either an opponent symbol in the way, or enough space to not go out of bounds), the evaluation function would then award 5 points for each “X” in the direction (not counting the original “X”) and 1 point for each empty space otherwise if there was not enough space for a winning condition then no points would be awarded for all the counted spaces. This was then calculated separately for the “O” input and was then the difference between the ‘X’ evaluation minus ‘O’ evaluation.

# Sections:
- How the algorithm determines what squares to check
- Etc.