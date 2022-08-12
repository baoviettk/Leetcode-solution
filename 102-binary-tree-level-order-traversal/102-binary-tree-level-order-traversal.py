# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = queue.Queue()
        result=[]
        if not root:
            return result
        if root.left:
            q.put(root.left)
        if root.right:
            q.put(root.right)
        result.append([root.val])
        while q.qsize()>0:
            cur=[]
            for _ in range(q.qsize()):
                node=q.get()
                cur.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            result.append(cur)
            
        return result