class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        
        def bfs(i, curr, target):
            if i==len(candidates) or target<=0:
                if target==0:
                    result.append(list(curr))
                return
            if target-candidates[i]>=0:
                curr.append(candidates[i])
                bfs(i+1,curr, target-candidates[i])
                curr.pop()
            i+=1
            while i<len(candidates) and candidates[i]==candidates[i-1]:
                i+=1

            bfs(i,curr,target)
        
        bfs(0,[], target)
        return result