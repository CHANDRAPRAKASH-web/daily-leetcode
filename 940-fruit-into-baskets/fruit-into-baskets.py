class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        a=defaultdict(int)
        max_count=0
        count=0
        for r in range(len(fruits)):
            a[fruits[r]]+=1
            while len(a)>2:
                count-=1
                if a[fruits[l]]==1:
                    del a[fruits[l]]
                else:
                    a[fruits[l]]-=1
                l+=1
            count+=1
            max_count=max(max_count,count)
        return max_count
        