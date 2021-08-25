# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
"""
Read characters from file
"""
# Read from file once
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        q = deque()
        i = 0
        
        while i < n:
            if q:
                buf[i] = q.popleft()
                i += 1
            else:
                q.extend([''] * 4)
                read4(q)

        return i
        

# Read from file repeatedly
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



class Solution:
    def __init__(self):
        self.buf4 = [''] *4
        self.i4 = 0
        self.n4 = 0
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        
        while i < n:
            if self.i4 == self.n4:
                self.i4 = 0
                self.n4 = read4(self.buf4 )
                if self.n4 == 0:
                    break
            
            buf[i] = self.buf4 [self.i4]
            self.i4 += 1
            i += 1
        
        return i
        