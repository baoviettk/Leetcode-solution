class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        preCrs={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preCrs[crs].append(pre)
        visited,cycle=set(),set()
        result=[]
        
        def canLearn(crs):
            # if preCrs[crs]==[]:
            #     if crs not in visited:
            #         result.append(crs)
            #     return
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in preCrs[crs]:
                if not canLearn(pre):
                    return False
            result.append(crs)
            visited.add(crs)
            cycle.remove(crs)
            return True
            
        for crs in range(numCourses):
            if not canLearn(crs):
                return []
        return result
        