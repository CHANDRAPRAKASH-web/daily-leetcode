class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix=[]
        cur=0

        for i in nums:
            cur+=i
            self.prefix.append(cur)
       
        
    def sumRange(self, left: int, right: int) -> int:
        r=self.prefix[right]
        if left==0:
            return r
        return r-self.prefix[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)