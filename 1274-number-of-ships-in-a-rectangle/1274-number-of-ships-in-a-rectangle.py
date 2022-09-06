# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def dnc(topRight, bottomLeft):
            if topRight.x<bottomLeft.x or topRight.y<bottomLeft.y:
                return 0
            if topRight.x==bottomLeft.x and topRight.y==bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))
                
            if not sea.hasShips(topRight,bottomLeft):
                return 0
            mid_x,mid_y=(topRight.x+bottomLeft.x)//2, (topRight.y+bottomLeft.y)//2
            count= dnc(Point(mid_x, topRight.y), Point(bottomLeft.x,mid_y+1))
            count+= dnc(topRight, Point(mid_x+1,mid_y+1))
            count+=dnc(Point(mid_x, mid_y), bottomLeft)
            count+=dnc(Point(topRight.x, mid_y), Point(mid_x+1,bottomLeft.y))
        
            return count
        
        return dnc(topRight, bottomLeft)