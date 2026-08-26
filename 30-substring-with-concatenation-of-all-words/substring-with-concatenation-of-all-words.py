class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target=len(words)
        word_length=len(words[0])
        res=[]
        words_count=defaultdict(int)
        for i in words:
            words_count[i]+=1
        
        for i in range(word_length):
            left,right=i,i
            s_map=defaultdict(int)
            count=0
            while right+word_length<=len(s):
                ss=s[right:right+word_length]
                right+=word_length
                if ss in words_count:
                    s_map[ss]+=1
                    count+=1

                    while s_map[ss]>words_count[ss]:
                        current_left=s[left:left+word_length]
                        s_map[current_left]-=1
                        count-=1
                        left+=word_length

                    if count==target:
                        res.append(left)
                else:
                    left=right
                    count=0
                    s_map.clear()
        return res

                
        
        