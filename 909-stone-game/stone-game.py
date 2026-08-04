class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo={}

        def dp(l,r):
            if l==r:
                return piles[l]

            if (l,r) in memo:
                return memo[(l,r)]

            left=piles[l]-dp(l+1,r)
            right=piles[r]-dp(l,r-1)
            memo[(l,r)]=max(left,right)

            return max(left,right)

        return dp(0,len(piles)-1)>0
       