"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        queue=[]
        if root==None:
           return root
        
        queue.append(root)
        leng= len(queue)
        while leng>0:
            for i in range(leng):
                current_node= queue.pop(0)
                if i==leng-1:
                    current_node.next= None
                else:
                    current_node.next=queue[0]
                if current_node.left!= None:
                    queue.append(current_node.left)
                if current_node.right!=None:
                    queue.append(current_node.right)     
            leng= len(queue)
        return root