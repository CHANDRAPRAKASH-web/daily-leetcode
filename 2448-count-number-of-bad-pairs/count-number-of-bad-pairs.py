class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        good=0
        f=defaultdict(int)
        for i,val in enumerate(nums):
            key=val-i
            good+=f[key]
            f[key]+=1
        return ((n*(n-1))//2)-good

       