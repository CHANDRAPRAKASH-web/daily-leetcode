class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a={}
        b={}
        for i in ransomNote:
            a[i]=1+a.get(i,0)

        for i in magazine:
            b[i]=1+b.get(i,0)

        for i in a:
            if a[i]>b.get(i,0):
                return False

        return True
        