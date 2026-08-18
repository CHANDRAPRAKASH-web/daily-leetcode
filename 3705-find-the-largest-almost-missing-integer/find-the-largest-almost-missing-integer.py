class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        a={}
        l=0
        r=k-1
        while r<len(nums):
            seen=set()
            for i in range(l,r+1):
                if nums[i] not in seen:
                    a[nums[i]]=1+a.get(nums[i],0)
                seen.add(nums[i])
                
            
            
                    
            l+=1
            r+=1

        value=-1
        for i in a:
            if a[i]==1:
                value=max(value,i)

        return value
