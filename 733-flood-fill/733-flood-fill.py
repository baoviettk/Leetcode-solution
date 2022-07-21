
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        queue=collections.deque()
        queue.appendleft((sr,sc))
        m,n=len(image),len(image[0])
        origin=image[sr][sc]
        while queue:
            current=queue.pop()
            if image[current[0]][current[1]]!=color and image[current[0]][current[1]]== origin :
                image[current[0]][current[1]]=color
                if current[0]+1<m:
                    queue.appendleft((current[0]+1,current[1]))
                if current[0]>0:
                    queue.appendleft((current[0]-1,current[1]))
                if current[1]+1<n:
                    queue.appendleft((current[0],current[1]+1))
                if current[1]>0:
                    queue.appendleft((current[0],current[1]-1))
        return image