class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n=len(s)
        f=[0]*26
        res=[]
        for i in s:
            f[ord(i)-ord('a')]+=1

        for i in range(n):
            valid=False
            t=target[i]
            for ci in range(26):
                c=chr(ci+ord('a'))
                if not f[ci] or c<t:
                    continue
                if c>t:
                    res.append(c)
                    f[ci]-=1
                    smallest=[]
                    for cci in range(26):
                        if f[cci]>0:
                            smallest.append(f[cci]*chr(cci+ord('a')))
                    return "".join(res+smallest)

                res.append(c)
                f[ci]-=1
                largest=[]
                for cci in range(25,-1,-1):
                    if f[cci]>0:
                        largest.append(f[cci]*chr(cci+ord('a')))
                if "".join(largest)>target[i+1:]:
                    valid=True
                    break
                f[ci]+=1
                res.pop()
            
            if not valid:
                return ""
        return ""



