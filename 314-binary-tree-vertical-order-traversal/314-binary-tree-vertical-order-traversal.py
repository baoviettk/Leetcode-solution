# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dic=defaultdict(lambda:[])
        MIN,MAX=9999,-9999
        q=collections.deque()
        q.append((root,0))
        res=[]
        
        while q:
            cur,index=q.popleft()
            dic[index].append(cur.val)
            if cur.left:
                q.append((cur.left,index-1))
            else:
                MIN=min(MIN, index)
            if cur.right:
                q.append((cur.right,index+1))
            else:
                MAX=max(MAX, index)
        for i in range(MIN, MAX+1):
            res.append(dic[i])          
        
        return res
            