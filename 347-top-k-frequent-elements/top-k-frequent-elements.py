class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}

        for i in nums:
            d[i]=1+d.get(i,0)
        
        sorted_d=dict(sorted(d.items(),key=lambda x:x[1], reverse=True))

        c=1
        a=[]

        for i in sorted_d:
            if c<=k:
                a.append(i)
                c+=1

        return a


