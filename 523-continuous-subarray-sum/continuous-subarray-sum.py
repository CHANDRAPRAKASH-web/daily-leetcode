class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        a={0:-1}
        s=0
        for i,num in enumerate(nums):
            s+=num
            r=s%k
            if r not in a:
                a[r]=i
            elif i-a[r]>1:
                return True
        return False
            
        