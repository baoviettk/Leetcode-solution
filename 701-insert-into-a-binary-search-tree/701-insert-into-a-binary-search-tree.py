# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val) 
        cur=root
        while True:
            if val > cur.val:
                if cur.right==None:
                    cur.right=TreeNode(val)
                    return root
                cur=cur.right
            else:
                if cur.left==None:
                    cur.left=TreeNode(val)
                    return root 
                cur=cur.left
                        
            
            