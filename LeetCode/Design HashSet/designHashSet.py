class MyHashSet:

    def __init__(self):
        self.myDict = dict()
        

    def add(self, key: int) -> None:
        self.myDict[key] = True
        

    def remove(self, key: int) -> None:
        if self.contains(key) :
            del self.myDict[key]
        

    def contains(self, key: int) -> bool:
        if key in self.myDict :
            return True
        else :
            return False
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)