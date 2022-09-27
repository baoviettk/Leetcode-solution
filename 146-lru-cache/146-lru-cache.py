class Node:
    def __init__(self,key, val):
        self.val=val
        self.key=key
        self.prev=None
        self.next=None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic={}
        self.left,self.right=Node(0,0), Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        

    def get(self, key: int) -> int:
        if key in self.dic:
            val=self.dic[key].val
            self.delete(key)
            self.add(key,val)
            return self.dic[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.delete(key)
        self.add(key,value)
        if len(self.dic)>self.capacity:
            self.delete(self.left.next.key)
        
    def delete(self, key):
        cur=self.dic[key]
        prev,nxt=cur.prev,cur.next
        prev.next=nxt
        nxt.prev=prev
        del self.dic[key]
    
    def add(self, key, val):
        new=Node(key,val)
        prev=self.right.prev
        self.right.prev=new
        new.prev,new.next=prev,self.right
        prev.next=new
        new.next
        self.dic[key]=new


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)