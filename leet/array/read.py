# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
"""

"""
class Solution:
    def __init__(self):
        self.q = deque()
    
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        
        while i < n:
            if self.q:
                buf[i] = self.q.popleft()
                i += 1
            else:
                self.q.extend([''] * 4)
                m = read4(self.q)
                if m == 0:
                    break
        return i