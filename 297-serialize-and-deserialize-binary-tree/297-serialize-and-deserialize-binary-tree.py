# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        result=[]
        def serializeNode(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.val))
            serializeNode(node.left)
            serializeNode(node.right)
            
        serializeNode(root)
        return ",".join(result)
        

    def deserialize(self, data):
        vals=data.split(",")
        self.i=0
        
        def dataToNode():
            if vals[self.i]=="N":
                self.i+=1
                return None
            
            root= TreeNode(int(vals[self.i]))
            self.i+=1
            root.left=dataToNode()
            root.right=dataToNode()
            
            return root
        return dataToNode()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))