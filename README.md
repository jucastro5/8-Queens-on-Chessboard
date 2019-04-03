# 8 Queens on a Chessboard?

From Wikipedia:
"The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal."

To run on cmd:
1) go to file directory
2) run "python queens.py"

Jupyter notebook file has unicoding that makes the chess board visualization cleaner. 

This program works by starting in the A column with a randomly selected row. It then updates the chessboard and moves to the next row, B. It then randomly selects a row from the B column that is 'valid' (aka where the queen in the A column cannot attack). It continues this all the way down to the final row. If the number of available valid spots become less than the number of remaining queens that need to be placed, the program starts over. Or, if it moves to a row with no valid spots, the program starts over. This is because there must be at least 1 queen per row and column. If it manages to place 8 queens, it saves the list of coordinates and restarts until the number of max restarts (iterations) is met. 

