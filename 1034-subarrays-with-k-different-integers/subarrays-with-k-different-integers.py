class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            freq=defaultdict(int)
            l=0
            r=0
            res=0
            for r in range(len(nums)):
                freq[nums[r]]+=1
                while len(freq)>k and l<r:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                if len(freq)<=k:
                    res+=(r-l+1)
            return res
        return atmost(k) - atmost(k-1)
            