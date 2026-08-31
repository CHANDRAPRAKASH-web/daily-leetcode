class Solution:
    def minDeletions(self, s: str) -> int:
        a=defaultdict(int)
        count=set()
        for i in s:
            a[i]+=1
        res=0
        for i in a:
            if a[i] not in count:
                count.add(a[i])
            else:
                for j in range(a[i]-1,-1,-1):
                    res+=1
                    if j not in count:
                       count.add(j)
                       break
        return res


        