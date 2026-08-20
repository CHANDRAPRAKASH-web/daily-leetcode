class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l=0
        n=len(p)
        a=defaultdict(int)
        p_count=Counter(p)
        res=[]
        for r in range(len(s)):
            a[s[r]]+=1
            if r-l+1 == n:
                if a==p_count:
                    res.append(l)
                if a[s[l]]==1:
                    del a[s[l]]
                else:
                    a[s[l]]-=1
                l+=1
        return res



    
        