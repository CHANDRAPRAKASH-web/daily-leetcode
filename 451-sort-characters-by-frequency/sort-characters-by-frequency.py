class Solution:
    def frequencySort(self, s: str) -> str:
        res=[]
        freq=[[] for _ in range(len(s)+1)]
        a={}
        for i in s:
            a[i]=1+a.get(i,0)
        
        for key,value in a.items():
            freq[value].append(key)

        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j*i)

        return "".join(res)


        