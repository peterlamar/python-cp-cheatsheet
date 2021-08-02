"""
time: c
space: c
"""
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strings:
            tmp = []
            for c in s:
                tmp.append((ord(s[0]) - ord(c))%26)
            ans[tuple(tmp)].append(s)
        return ans.values()

    def groupStrings(self, strs : List[str]) -> List[List[str]]:
        hm = collections.defaultdict(list)
        for s in strs:
            key = ""
            for c in s:
                key = key + str((ord(s[0])- ord(c))%26)
            hm[key].append(s)
        return hm.values()