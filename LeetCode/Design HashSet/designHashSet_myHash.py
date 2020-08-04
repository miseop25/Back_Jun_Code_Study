class MyHashSet:

    def __init__(self):
        self.myDict = [False]*1000001
        

    def add(self, key: int) -> None:
        self.myDict[key] = True
        

    def remove(self, key: int) -> None:
        if self.contains(key) :
            self.myDict[key] = False
        

    def contains(self, key: int) -> bool:
        return self.myDict[key]




"""
Returns true if this set contains the specified element
"""
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)