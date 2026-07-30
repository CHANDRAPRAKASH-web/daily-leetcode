class Solution:
    def minimumPushes(self, word: str) -> int:
        count=0
        current_cost=1
        total_cost=0
        for i in range(len(word)):
            if count==8:
                count=0
                current_cost+=1

            total_cost+=current_cost
            count+=1

        return total_cost
            

        