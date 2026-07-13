class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in accounts:
            if sum(i)>m:
                m=sum(i)
        return m