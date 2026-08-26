class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target=defaultdict(int)
        window=defaultdict(int)
        for i in t:
            target[i]+=1
        need=len(target)
        current=0
        l=0
        res_length=float('inf')
        for r in range(len(s)):
            if s[r] in target:
                window[s[r]]+=1
                if window[s[r]]==target[s[r]]:
                    current+=1
            while current==need:
                if r-l+1<res_length:
                    left,right=l,r
                    res_length=r-l+1
                if s[l] in target:
                    window[s[l]]-=1
                    if window[s[l]]<target[s[l]]:
                        current-=1
                l+=1

        return s[left:right+1] if res_length!=float('inf') else ""


        