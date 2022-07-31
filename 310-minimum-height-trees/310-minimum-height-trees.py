import queue

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        result=[]
        adj = {i: set() for i in range(n)}
        degree = [0] * n
        q = queue.Queue()
        if n == 0:
            return -1
        if n == 1:
            return [0]
        for edge in edges:
            e1, e2 = edge[0], edge[1]
            degree[e1] += 1
            degree[e2] += 1
            adj[e1].add(e2)
            adj[e2].add(e1)

        for e in range(n):
            if degree[e] == 1:
                q.put(e)

        while n > 2:
            size = q.qsize()
            n -= size
            for _ in range(size):
                top_edge = q.get()
                next_edge = list(adj[top_edge])[0]
                degree[top_edge] -= 1
                degree[next_edge] -= 1
                adj[next_edge].remove(top_edge)
                if degree[next_edge] == 1:
                    q.put(next_edge)

        while q.qsize()>0:
            result.append(q.get())

        return result