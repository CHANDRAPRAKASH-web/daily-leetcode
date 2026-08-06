class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=0
        r=len(needle)-1
        while r<len(haystack):
            a=haystack[l:r+1]
            if a==needle:
                return l
            l+=1
            r+=1

        return -1

        