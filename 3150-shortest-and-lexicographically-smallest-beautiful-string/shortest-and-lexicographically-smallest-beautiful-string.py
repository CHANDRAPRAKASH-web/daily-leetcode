class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        ones=0
        res=""
        for r in range(len(s)):
            if s[r]=='1':
                ones+=1
            while l<r and (ones>k or s[l]=='0'):
                if s[l]=='1':
                    ones-=1
                l+=1
            if ones==k:
                ss=s[l:r+1]
                if not res or len(ss)<len(res) or ((len(ss)==len(res)) and ss<res):
                    res=ss
        return res
           