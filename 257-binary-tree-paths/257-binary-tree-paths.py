# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result=[]
        cur_path=[]
        def btk(new_root):
            if not new_root:
                return
            cur_path.append(str(new_root.val))
            if not new_root.left and not new_root.right:
                result.append("->".join(cur_path))
            btk(new_root.left)
            btk(new_root.right)
            cur_path.pop()
        
        btk(root)
        return result
        