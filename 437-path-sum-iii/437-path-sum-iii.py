# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        dic={0:1}
        return self.findAllPath(root, 0,dic,targetSum)
        
    
    def findAllPath(self,root, current_sum, dic, target_sum):
        if root==None:
            return 0
        current_sum+=root.val
        key = current_sum-target_sum
        count=dic.get(key,0)
        if current_sum not in dic.keys():
            dic[current_sum]=0
        dic[current_sum]+=1
        count+=self.findAllPath(root.left, current_sum,dic,target_sum)+ self.findAllPath(root.right, current_sum,dic,target_sum)
        dic[current_sum]-=1
        return count
        
        
        