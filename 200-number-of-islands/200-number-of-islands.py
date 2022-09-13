class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        MAX_ROW, MAX_COL= len(grid), len(grid[0])
        
        def mark(r,c):
            if r<MAX_ROW and c<MAX_COL and r>-1 and c>-1 and grid[r][c]=="1":
                grid[r][c]="2"
                mark(r+1,c)
                mark(r-1,c)
                mark(r,c+1)
                mark(r,c-1)
            return
        result=0
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if grid[i][j]=="1":
                    result+=1
                    mark(i,j)
        return result
                    