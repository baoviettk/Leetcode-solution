class Node:
    
    def __init__(self,key:int, val:int):
        self.key=key
        self.val=val
        self.next, self.prev=None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        
        self.left,self.right=Node(0,0), Node(0,0)
        self.left.next, self.right.prev=self.right, self.left
        
    def add(self, node: Node): #to the right
        prev,right=self.right.prev, self.right
        prev.next, node.next=node,right
        node.prev, right.prev=prev,node

    def remove(self, node:Node):
        prev, right=node.prev, node.next
        prev.next, right.prev=right, prev
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.add(self.cache[key])
        if len(self.cache)>self.cap:
            remove_node=self.left.next
            del self.cache[remove_node.key]
            self.remove(remove_node)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)