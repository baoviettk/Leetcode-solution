# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        result=[]
        queue=[]
        if root==None:
            return result
        
        queue.append(root)
        left_to_right=True
        while len(queue)>0:
            current_layer=deque()
            for i in range(len(queue)):
                current_node= queue.pop(0)
                if current_node.left!= None:
                    queue.append(current_node.left)
                if current_node.right!=None:
                    queue.append(current_node.right)
                if left_to_right:
                    current_layer.append(current_node.val)
                else:
                    current_layer.appendleft(current_node.val)
            left_to_right = not left_to_right
            
            result.append(current_layer)
        
        return result
        