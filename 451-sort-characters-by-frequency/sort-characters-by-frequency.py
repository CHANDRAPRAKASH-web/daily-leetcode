class Solution:
    def frequencySort(self, s: str) -> str:
        res=[]
        freq=[[] for _ in range(len(s)+1)]
        a={}
        for i in s:
            a[i]=1+a.get(i,0) # t:1 r:1 e:2
        
        for key,value in a.items():
            freq[value].append(key) # 1:t,r 2:e 

        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j*i) # [e,e,t,r] * s="" s+=j*i

        return "".join(res)


        