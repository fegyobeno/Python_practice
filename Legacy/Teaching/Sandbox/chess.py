import numpy as np
board = np.array([np.zeros(8) for _ in range(8)])

pieces = {
    "0": "👑"  
}

def draw_board(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0.:
                print(pieces[str(int(board[i][j]))], end="|")
        print()

print(board.shape)
draw_board(board=board)