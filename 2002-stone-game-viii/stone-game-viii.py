class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n=len(stones)
        prefix=[0]*n
        prefix[0]=stones[0]
        for i in range(1,n):
            prefix[i]=prefix[i-1]+stones[i]
        cache={}
        def dp(i):
            if i==n-1:
                return prefix[i]
            if n in cache:
                return cache[n]
            option1=dp(i+1)
            option2=prefix[i]-dp(i+1)
            cache[n]=max(option1,option2)
            return max(option1,option2)
        
        return dp(1)




        