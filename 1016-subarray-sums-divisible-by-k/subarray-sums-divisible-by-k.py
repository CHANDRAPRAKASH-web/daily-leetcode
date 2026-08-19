class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        a={0:1}
        s=0
        count
        for i in nums:
            s+=i
            r=s%k
            count+=a.get(r,0)
            a[r]=1+a.get(r,0)
        return count
           

        