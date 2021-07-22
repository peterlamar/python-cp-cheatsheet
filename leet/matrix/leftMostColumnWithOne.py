class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        R, C = binaryMatrix.dimensions()
        foundOne = -1
        rtn = C - 1
        for r in range(R):
            for c in range(rtn, -1, -1):
                if binaryMatrix.get(r,c) == 1:
                    rtn = c
                    foundOne = c
                else:
                    break
        
        if foundOne == -1:
            return -1
        
        return rtn

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        y,x = binaryMatrix.dimensions()
        foundOne = False
        
        r = x-1
        for y1 in range(y):
            while r >= 0 and binaryMatrix.get(y1, r) == 1:
                r -= 1
                foundOne = True
            if r == -1:
                return 0
        
        if foundOne == False:
            return -1
        else:
            return r+1


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        y,x = binaryMatrix.dimensions()
        
        cury=0
        curx=x-1
        
        while cury < y and curx >= 0:
            if binaryMatrix.get(cury, curx):
                curx -= 1
            else:
                cury += 1
        
        if curx == x-1:
            return -1
        else:
            return curx + 1

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        res, (y, x) = -1, binaryMatrix.dimensions()
        print("x :", x)

        for i in range(y):
            for j in range(res % x, -1, -1):
                if binaryMatrix.get(i, j): res = j
                else: break

        return res

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        y, x =  binaryMatrix.dimensions()
        foundOne = False
        res = x -1
        
        for i in range(y):
            for j in range(res, -1, -1):
                if binaryMatrix.get(i, j): 
                    res = j
                    foundOne = True
                else: 
                    break

        if foundOne == False:
            return -1
                    
        return res