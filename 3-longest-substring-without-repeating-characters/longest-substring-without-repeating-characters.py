class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        length=0
        res=set()

        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l+=1

            w=(r-l)+1
            length=max(w,length)
            res.add(s[r])

        return length

     