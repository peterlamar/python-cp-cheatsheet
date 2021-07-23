class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    
        def dfs(path:str, y:int, x:int):
            # check for word
            # mark visited
            # go to valid neighbors
            if len(path) == 0:
                return True 
            if x < 0 or y < 0 or y == len(board) or x == len(board[y]) or board[y][x] != path[:1]:
                return False
            
            tmp = board[y][x]
            board[y][x] = '#'
            
            if dfs(path[1:], y-1, x) or \
            dfs(path[1:], y+1, x) or \
            dfs(path[1:], y, x+1) or \
            dfs(path[1:], y, x-1):
                return True
            
            board[y][x] = tmp 
            
       # double loop to check all starting places
        for y in range(0, len(board)):
            for x in range(0, len(board[y])):
                if dfs(word, y, x):
                    return True
                
        return False;

class Solution:
    def exist(self, board:List[List[str]], word:str) -> bool:
        
        def dfs(path:str, y:int, x:int):
            if len(path) == 0:
                return True
            
            if (y<0 or x<0 or y==len(board) or \
                x==len(board[y]) or board[y][x] != path[0]):
                return False
            
            tmp = board[y][x]
            board[y][x] = '#'
            
            if dfs(path[1:], y-1, x) or \
               dfs(path[1:], y+1, x) or \
               dfs(path[1:], y, x-1) or \
               dfs(path[1:], y, x+1):
                return True
            
            board[y][x] = tmp
            
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                if dfs(word, y, x):
                    return True
        
        return False
        