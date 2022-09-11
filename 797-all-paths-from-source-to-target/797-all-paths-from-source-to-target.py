class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        cur=[0]
        result=[]
        def dfs(start):
            for des in graph[start]:
                if des ==len(graph)-1:
                    temp=list(cur)
                    temp.append(des)
                    result.append(temp)
                else:
                    cur.append(des)
                    dfs(des)
                    cur.pop()
        dfs(0)
        return result
                    
            