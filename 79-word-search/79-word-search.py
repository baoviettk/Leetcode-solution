class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MAX_ROW,MAX_COL=len(board),len(board[0])
        def dfs(r,c, i):
            if i == len(word):
                return True
            if r==MAX_ROW or c==MAX_COL or r<0 or c<0 or board[r][c]!=word[i]:
                return False
            temp=board[r][c]
            board[r][c]='#'

            result= dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
            board[r][c]=temp
            return result
        
        for r in range(MAX_ROW):
            for c in range(MAX_COL):
                if dfs(r,c,0): return True
        return False