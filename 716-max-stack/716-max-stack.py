class MaxStack:

    def __init__(self):
        self.stack=[]
        self.heap=[]
        self.not_clean=set()
        self.cur_id=0

    def push(self, x: int) -> None:
        heappush(self.heap,[-x,self.cur_id])
        self.stack.append([x,self.cur_id])
        self.cur_id-=1

    def pop(self) -> int:
        [val,id]=self.stack.pop()
        self.not_clean.add(id)
        self.clean_data()
        return val

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return -self.heap[0][0]

    def popMax(self) -> int:
        [val,id]=heappop(self.heap)
        self.not_clean.add(id)
        self.clean_data()
        return -val
    
    def clean_data(self):
        while self.stack and self.stack[-1][1] in self.not_clean:
            self.not_clean.remove(self.stack.pop()[1])
        while self.heap and self.heap[0][1] in self.not_clean:
            self.not_clean.remove(heappop(self.heap)[1])
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()