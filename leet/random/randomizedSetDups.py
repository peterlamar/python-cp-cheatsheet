class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.pos = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """

        self.data.append(val)
        self.pos[val].add(len(self.data) - 1)
        
        return len(self.pos[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.pos[val]: return False
            
        oldValPos = self.pos[val].pop() 
        endV = self.data[-1]

        self.data[oldValPos] = endV
        self.pos[endV].add(oldValPos)
        self.pos[endV].discard(len(self.data) - 1)

        self.data.pop()
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.data)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()