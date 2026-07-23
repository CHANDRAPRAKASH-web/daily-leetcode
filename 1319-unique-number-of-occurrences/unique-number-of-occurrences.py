class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a={}
        b=set()
        for i in arr:
            a[i]=1+a.get(i,0)

        for i in a:
            if a[i] in b:
                return False
            b.add(a[i])

        return True
        