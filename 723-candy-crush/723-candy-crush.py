class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board:
            return board
        done=False
        while not done:
            done=True
            #Crush row
            for r in range(len(board)):
                for c in range(len(board[0])-2):
                    num1= abs(board[r][c])
                    num2= abs(board[r][c+1])
                    num3= abs(board[r][c+2])
                    if  num1==num2 and num2==num3 and num1!=0:
                        board[r][c]=-num1
                        board[r][c+1]=-num2
                        board[r][c+2]=-num3
                        done=False
            #Crush column
            for c in range(len(board[0])):
                for r in range(len(board)-2):
                    num1= abs(board[r][c])
                    num2= abs(board[r+1][c])
                    num3= abs(board[r+2][c])
                    if  num1==num2 and num2==num3 and num1!=0:
                        board[r][c]=-num1
                        board[r+1][c]=-num2
                        board[r+2][c]=-num3
                        done=False
            #Gravity
            for c in range(len(board[0])):
                replace=len(board)-1
                for r in range(len(board)-1,-1,-1):
                    if board[r][c]>0:
                        board[replace][c]= board[r][c]
                        replace-=1
                for r in range(replace,-1,-1):
                    board[r][c]=0
                    
        return board
            
                    