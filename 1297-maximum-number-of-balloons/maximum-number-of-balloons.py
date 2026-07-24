class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon='balloon'

        for i in text:
            if i in balloon:
                counter[i]+=1

        for c in balloon:
            if c not in counter:
                return 0
        
        return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])