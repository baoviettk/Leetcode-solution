class Solution(object):
    def snakesAndLadders(self, board):
        board.reverse()
        l=len(board)

        def strc(square):
            r=(square-1)//l
            c=(square-1)%l
            if r%2:
                c=l-c-1
            return [r,c]
            
        q= deque() #[square, cost]
        result=0
        q.append([1,0])
        
        while q:
            sq,co=q.popleft()
            for i in range(1,7):
                nxt_sq=sq+i
                r,c=strc(nxt_sq)
                if board[r][c]==-2:
                    continue
                if board[r][c]!=-1:
                    nxt_sq=board[r][c]
                if nxt_sq==l*l:
                    return co+1
                board[r][c]=-2
                q.append([nxt_sq,co+1])
        return -1
            
        
        
        
        
        