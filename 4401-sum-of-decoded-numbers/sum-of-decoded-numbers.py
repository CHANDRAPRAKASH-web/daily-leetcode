class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        count=0
        for i in nums:
            width=i%10
            d=i//10
            d=str(d)
            x=int(d[:width])
            y=int(d[width:])
            count=(count+pow(x,y,10**9+7))%(10**9+7)
        
        return count


        