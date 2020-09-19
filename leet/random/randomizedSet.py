class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.data.append(val)
            self.pos[val] = len(self.data) - 1
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            posToDel = self.pos[val]
            endv = self.data[-1]
            
            self.pos[endv] = posToDel
            self.data[posToDel] = endv
            
            self.data.pop()
            self.pos.pop(val,0)
            return True
            

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()