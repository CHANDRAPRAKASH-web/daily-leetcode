class Solution:
    def firstUniqChar(self, s: str) -> int:
        h={}
        for c in s:
            h[c]=1+h.get(c,0)

        for i , c in enumerate(s):
            if h[c]==1:
                return i
        return -1
            
        