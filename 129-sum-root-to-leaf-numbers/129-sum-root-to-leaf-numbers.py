# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        return self.calculateSum(root,0)
        
    def calculateSum(self, root, current):
        if root == None:
            # print('total:' +str(total))
            return 0
        
        current= current*10+ root.val
        print ('current: ' + str(current))
        print ('val: ' + str(root.val))
        if root.left == None and root.right==None:
            # print ('current when added: ' + str(current))
            return current
        else:
            return self.calculateSum(root.left, current)+ self.calculateSum(root.right, current)
        current= current//10