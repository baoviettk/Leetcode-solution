class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirX, dirY=0,1
        x,y=0,0
        for i in instructions:
            if i=='G':
                x+=dirX
                y+=dirY
            elif i=='L':
                dirX,dirY= -dirY,dirX
            else:
                dirX,dirY= dirY,-dirX
        
        return (x,y)==(0,0) or not(dirX,dirY)==(0,1)