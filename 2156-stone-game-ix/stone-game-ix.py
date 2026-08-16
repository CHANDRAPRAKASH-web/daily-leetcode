class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        a={0:0,1:0,2:0}
        for i in stones:
            a[i%3]=1+a.get(i%3,0)

        if a[0]%2==0 and a[1]>=1 and a[2]>=1:
            return True
        elif a[0]%2==1 and abs(a[1]-a[2])>2:
            return True
        else:
            return False
        