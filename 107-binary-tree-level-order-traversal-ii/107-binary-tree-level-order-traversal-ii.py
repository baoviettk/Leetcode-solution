# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        result=[]
        queue=[]
        if root==None:
            return result
        
        queue.append(root)
        
        if len(queue)>0:
            self.add_layer(queue, result)            
            
        return result
        
    def add_layer(self, queue, result):
        current_layer=[]
        for i in range(len(queue)):
            current_node= queue.pop(0)
            if current_node.left!= None:
                queue.append(current_node.left)
            if current_node.right!=None:
                queue.append(current_node.right)
            current_layer.append(current_node.val)
        if len(queue)>0:
            self.add_layer(queue,result)
        result.append(current_layer)
        return
        
        
        