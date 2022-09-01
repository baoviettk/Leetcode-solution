class RandomizedSet:

    def __init__(self):
        self.map={}
        self.list=[]

    def insert(self, val: int) -> bool:
        present= val in self.map
        if not present:
            self.map[val]=len(self.list)
            self.list.append(val)
            return True
        return False
    def remove(self, val: int) -> bool:
        present= val in self.map
        if present:
            i=self.map[val]
            last_val=self.list[-1]
            self.list[i]=last_val
            self.list.pop()
            self.map[last_val]=i
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()