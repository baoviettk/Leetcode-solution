class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, alt=set(),set()
        max_x, max_y=len(heights), len(heights[0])
        result=[]
        
        def expandVisit(x,y,visit,prev):
            if (x,y) in visit or x<0 or y<0 or x>=max_x or y>=max_y or heights[x][y]<prev:
                return
            visit.add((x,y))
            expandVisit(x+1,y,visit,heights[x][y])
            expandVisit(x-1,y,visit,heights[x][y])
            expandVisit(x,y+1,visit,heights[x][y])
            expandVisit(x,y-1,visit,heights[x][y])
        
        for i in range(max_x):
            expandVisit(i,0,pac,-1)
            expandVisit(i,max_y-1,alt,-1)

        for i in range(max_y):
            expandVisit(0,i,pac,-1)
            expandVisit(max_x-1,i,alt,-1)
            
        for x in range(max_x):
            for y in range(max_y):
                if (x,y) in pac and (x,y) in alt:
                    result.append([x,y])
        return result