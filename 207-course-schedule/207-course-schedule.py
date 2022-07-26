class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preCrs={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preCrs[crs].append(pre)
        visitSet=set()
        
        def canTake(crs):
            if preCrs[crs]==[]:
                return True
            if crs in visitSet:
                return False
            visitSet.add(crs)
            
            for pre in preCrs[crs]:
                if not canTake(pre):
                    return False
                
            visitSet.remove(crs)
            preCrs[crs]=[]
            return True
            
        for crs in range(numCourses):
            if not canTake(crs):
                return False
        return True
        