class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={i:[] for i in range(numCourses)}
        cur=set()
        for crs, preC in prerequisites:
            pre[crs].append(preC)
            
        def canTake(crs):
            if pre[crs]==[]:
                return True
            if crs in cur:
                return False
            cur.add(crs)
            for preC in pre[crs]:
                if not canTake(preC):
                    return False
            cur.remove(crs)
            pre[crs]=[]
            
            return True
        
        for i in range(numCourses):
            if not canTake(i):
                return False
        return True