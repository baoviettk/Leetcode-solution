# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result=root.val
        def maxNode(node):
            if not node:
                return 0
            left= max(0,maxNode(node.left))
            right= max(0,maxNode(node.right))
            self.result=max(self.result, left+right+node.val)
            return max(left, right)+node.val
        
        maxNode(root)
        return self.result