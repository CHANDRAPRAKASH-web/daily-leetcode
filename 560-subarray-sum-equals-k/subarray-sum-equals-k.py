class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a={}
        a[0]=1
        prefix=0
        count=0

        for i in nums:
            prefix+=i
            value=prefix-k
            if value in a:
                count+=a[value]
            a[prefix]=1+a.get(prefix,0)

        return count
       