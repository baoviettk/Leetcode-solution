# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        all_path=[]
        self.findAllPath(root, all_path,[],targetSum)
        return all_path
    
    def findAllPath(self,root, all_path, current_path, target_sum):
        if root==None:
            return
        current_path.append(root.val)
        if root.left== None and root.right == None and root.val==target_sum:
            all_path.append(list(current_path))
        
        else:
            self.findAllPath(root.left,all_path, current_path, target_sum-root.val)
            self.findAllPath(root.right,all_path, current_path, target_sum-root.val)
        
        del current_path[-1]