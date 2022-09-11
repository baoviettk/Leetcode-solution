class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        cur=[0]
        result=[]
        def dfs(start):
            for des in graph[start]:
                cur.append(des)
                if des ==len(graph)-1:
                    result.append(list(cur))
                else:
                    dfs(des)
                cur.pop()
        dfs(0)
        return result
                    
            