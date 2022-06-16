# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        queue=[]
        if root==None:
            return 0
        queue.append(root)
        depth=0
        while(queue):
            leng=len(queue)
            depth+=1
            for i in range(leng):
                current=queue.pop(0)
                if(current.left == None) and (current.right==None):
                    return depth
                if current.left !=None:
                    queue.append(current.left)
                if current.right !=None:
                    queue.append(current.right)

        return -1
                    