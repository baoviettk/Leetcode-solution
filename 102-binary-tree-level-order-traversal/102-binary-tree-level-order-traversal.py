# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        result=[]
        if not root:
            return result
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
        result.append([root.val])
        while q:
            cur=[]
            for _ in range(len(q)):
                node=q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(cur)
            
        return result