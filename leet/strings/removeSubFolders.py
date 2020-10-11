class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if not folder:
            return
        folder.sort()
        ans, prev = [], folder[0] + '/'
        
        for f in folder:
            if not f.startswith(prev):
                ans.append(f)
                prev = f + '/'
        return ans

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        seen = set()
        for f in folder:
            for i in range(2, len(f)):
                if f[i] == '/' and f[: i] in seen:
                    break
            else:
                seen.add(f)
        return list(seen)