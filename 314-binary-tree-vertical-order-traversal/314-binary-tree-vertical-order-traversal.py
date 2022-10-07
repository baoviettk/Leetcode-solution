# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        MIN=9999
        MAX=-9999
        dic=defaultdict(lambda:[])
        res=[]
        if not root:
            return root
        q=collections.deque()
        q.append((root,0))
        while q:
            node, x=q.popleft()
            dic[x].append(node.val)
            if node.left:
                q.append((node.left,x-1))
            else:
                MIN=min(MIN, x)
                
            if node.right:
                q.append((node.right,x+1))
            else:
                MAX=max(MAX, x)
        for i in range(MIN, MAX+1):
            res.append(dic[i])
        
        return res
            