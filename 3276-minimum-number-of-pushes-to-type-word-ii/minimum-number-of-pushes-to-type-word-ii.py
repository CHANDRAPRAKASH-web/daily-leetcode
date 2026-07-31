class Solution:
    def minimumPushes(self, word: str) -> int:
        
        b={}
        count=0
        for i in word:
            b[i]=1+b.get(i,0)

        a=sorted(b.values(),reverse=True)

        for index,val in enumerate(a):
            count+=val*((index//8)+1)

        return count

        