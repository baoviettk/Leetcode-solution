class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        COL, ROW=len(board[0]),len(board)
        done=False
        while not done:
            done=True
#             find horizontal
            if COL>2:
                for row in range(ROW):
                    for x in range(COL-2):
                        if abs(board[row][x])==abs(board[row][x+1]) and abs(board[row][x+1])==abs(board[row][x+2]) and board[row][x]!=0:
                            val=-abs(board[row][x])
                            board[row][x]=val
                            board[row][x+1]=val
                            board[row][x+2]=val
                            done=False
#           find vertical
            for col in range(COL):
                for y in range(ROW-2):
                    if abs(board[y][col])==abs(board[y+1][col]) and abs(board[y+1][col])==abs(board[y+2][col]) and board[y][col]!=0:
                        val=-abs(board[y][col])
                        board[y][col]=val
                        board[y+1][col]=val
                        board[y+2][col]=val
                        done=False
#            Drop
            for x in range(COL):
                hole=ROW-1
                for y in range(ROW-1,-1,-1):
                    if board[y][x]<=0:
                        continue
                    board[y][x],board[hole][x]=board[hole][x],board[y][x]
                    hole-=1
                for y in range(0,hole+1):
                    board[y][x]=0
                
        return board
                
                