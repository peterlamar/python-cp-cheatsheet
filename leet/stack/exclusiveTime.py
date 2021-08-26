"""
time: n
space: n/2
Exclusive Time of Functions
"""

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        prev = 0
        stk = []
        
        for l in logs:
            fn, type, time = l.split(':')
            
            time = int(time)
            fn = int(fn)
            
            if type == "start":
                if stk:
                    ans[stk[-1]] += time - prev
                stk.append(fn)
                prev = time
            else:
                ans[stk.pop()] += time - prev + 1
                prev = time + 1
                
        return ans
            


"""
"""
class SuperStack(object):
    def __init__(self):
        self.A = []
    def append(self, x):
        self.A.append([x, 0])
    def pop(self):
        x, y = self.A.pop()
        if self.A:
            self.A[-1][1] += y
        return x + y
    def add_across(self, y):
        if self.A:
            self.A[-1][1] += y

class Solution:
    def exclusiveTime(self, N, logs):
        ans = [0] * N
        stack = SuperStack()

        for log in logs:
            fn, typ, time = log.split(':')
            fn, time = int(fn), int(time)

            if typ == 'start':
                stack.append(time)
            else:
                delta = time - stack.pop() + 1
                ans[fn] += delta
                stack.add_across(delta)

        return ans
            