class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        r=0
        length=0
        a={}
        for r in range(len(s)):
            a[s[r]]=1+a.get(s[r],0)
            while a[s[r]]>2:
                a[s[l]]-=1
                l+=1
            length=max(length,r-l+1)

        return length
        