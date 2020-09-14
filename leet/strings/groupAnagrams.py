"""
time: wc*lgk
space:wc
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            key = tuple(sorted(w))
            d[key].append(w)
        return d.values()

"""
time: wc
space:wc
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord('a')] += 1
            key = tuple(cnt)
            d[key].append(w)
        return d.values()