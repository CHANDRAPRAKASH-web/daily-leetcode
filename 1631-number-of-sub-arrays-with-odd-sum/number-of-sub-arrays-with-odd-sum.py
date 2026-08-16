class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum=0
        even_sum=0
        odd_sum=0
        res=0

        for i in arr:
            cur_sum+=i
            if cur_sum%2==1:
                res+=1
                res+=even_sum
                odd_sum+=1
            else:
                res+=odd_sum
                even_sum+=1

        return (res)%((10**9)+7)

           
        