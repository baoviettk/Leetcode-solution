class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result=[]
        cur=[0]
        n=len(graph)
        def dfs(start):
            for i in graph[start]:
                cur.append(i)
                if i==n-1:
                    result.append(list(cur))
                else:
                    dfs(i)
                cur.pop()
        
        dfs(0)
        return result
                    
        
    
#     time: O(n+v)
#     space: O(n)
                    
            