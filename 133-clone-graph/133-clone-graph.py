"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new={}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            
            new_node=Node(node.val)
            old_to_new[node]=new_node
            for nei in node.neighbors:
                new_node.neighbors.append(clone(nei))
            
            return new_node
        
        return clone(node) if node else None