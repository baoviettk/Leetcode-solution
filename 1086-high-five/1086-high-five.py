class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        dic=defaultdict(lambda: [])
        result=[]
        for id, score in items:
            dic[id].append(score)
        for k in dic:
            result.append([k, sum(heapq.nlargest(5,dic[k]))//5])
        return sorted(result, key= lambda x: x[0])