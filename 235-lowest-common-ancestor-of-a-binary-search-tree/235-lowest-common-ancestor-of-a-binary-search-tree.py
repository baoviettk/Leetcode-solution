# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if not root:
                return None
            if (root.val>=p.val and root.val<=q.val) or (root.val>=q.val and root.val<=p.val):
                return root
            if (root.val>=p.val and root.val>=q.val):
                root=root.left
            else:
                root=root.right