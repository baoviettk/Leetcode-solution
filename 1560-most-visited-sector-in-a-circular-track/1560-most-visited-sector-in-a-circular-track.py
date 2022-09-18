class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        result=[]
        st,fn=rounds[0],rounds[-1]
        if fn>=st:
            for i in range(st,fn+1):
                result.append(i)
            return result
        for i in range(1,fn+1):
            result.append(i)
        for i in range(st,n+1):
            result.append(i)
        return result