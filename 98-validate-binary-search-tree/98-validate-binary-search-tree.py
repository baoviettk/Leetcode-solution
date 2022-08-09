# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def traverse(cur,upper, lower):
            if not cur:
                return True
            if cur.val>=upper or cur.val<=lower:
                return False
            
            return traverse(cur.left,cur.val, lower) and traverse(cur.right,upper, cur.val)
        
        return traverse(root,float('inf'),float('-inf'))
            