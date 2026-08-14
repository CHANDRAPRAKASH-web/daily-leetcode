class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l,r=0,0
        length=0
        freq={}
        for r,char in enumerate(s):
            freq[char]=1+freq.get(char,0)
            while freq[char]>2:
                freq[s[l]]-=1
                l+=1
            length=max(length,r-l+1)

        return length
        