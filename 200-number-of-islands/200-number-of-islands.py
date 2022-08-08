class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_x,max_y=len(grid), len(grid[0])
        result=0
        
        def markVisited(i,j):
            if i>=max_x or j>=max_y or i<0 or j<0 or grid[i][j]!="1":
                return
            grid[i][j]="2"
            markVisited(i-1,j)
            markVisited(i+1,j)
            markVisited(i,j-1)
            markVisited(i,j+1)
            
        
        for i in range(max_x):
            for j in range(max_y):
                if grid[i][j]=="1":
                    markVisited(i,j)
                    result+=1
                
        return result
                    