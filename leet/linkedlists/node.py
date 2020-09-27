class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.st = set()

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dct = {}
        
    def add_prev(self, node, key):
        if node.val-1 != node.prev.val:
            new = Node(node.val - 1)
            new.prev, new.next = node, node.next 
            new.prev.next = new.next.prev = new
        else:
            new = node.prev 
        
        new.st.add(key)
        return new
            
    def add_next(self, node, key):
        if node.val+1 != node.next.val:
            new = Node(node.val + 1)
            new.prev, new.next = node, node.next 
            new.prev.next = new.next.prev = new
        else:
            new = node.next
        
        new.st.add(key)
        return new

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.dct:
            self.dct[key] = self.add_next(self.head, key) 
        else:
            node = self.dct[key]
            self.dct[key] = self.add_next(node,key)
            node.st.remove(key)
            if not node.st:
                node.prev.next, node.next.prev = node.next, node.prev

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.dct:
            node = self.dct[key]
            node.st.remove(key)
            del self.dct[key]
            if node.val > 1:
                self.dct[key] = self.add_prev(node, key)
            if not node.st:
                node.prev.next, node.next.prev = node.next, node.prev

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.tail.prev.st:
            return ""
        return next(iter(self.tail.prev.st))
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.head.next.st:
            return ""
        return next(iter(self.head.next.st))



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()