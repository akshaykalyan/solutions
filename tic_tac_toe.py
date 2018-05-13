def isSolved(board):
    print(board)
    for x in range(3):
        if board[x][0]==board[x][1]==board[x][2]:
            if board[x][0]!=0:  
                return board[x][0]
        elif board[0][x]==board[1][x]==board[2][x]:
            if board[0][x]!=0:  
                return board[0][x]
    if board[0][0]==board[1][1]==board[2][2]:
        if board[1][1]!=0:  
            return board[1][1]
    elif board[0][2]==board[1][1]==board[2][0]:
        if board[1][1]!=0:
            return[1][1]
    for x in range(3):
        for y in range(3):
            if 0 == board[x][y]:
                return -1
    return 0
print(isSolved([[0, 1, 1], [2, 0, 2], [2, 1, 0]]))
