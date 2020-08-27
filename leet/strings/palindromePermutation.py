class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        st = set()
        
        for c in s:
            if c in st:
                st.remove(c)
            else:
                st.add(c)
        
        return len(st) <= 1