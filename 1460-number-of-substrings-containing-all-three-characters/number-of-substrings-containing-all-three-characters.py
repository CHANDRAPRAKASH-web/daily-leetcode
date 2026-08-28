class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        n=len(s)
        ans=0
        a={}
        for r in range(len(s)):
            a[s[r]]=1+a.get(s[r],0)
            while len(a)==3:
                ans+=n-r
                a[s[l]]-=1
                if a[s[l]]==0:
                    del a[s[l]]
                l+=1
        return ans
            
        