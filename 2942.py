class Solution:
    def findWordsContaining(self, w: List[str], x: str) -> List[int]:
        l=[]
        for i in range(len(w)):
            if(x in w[i]):
                l.append(i)
        # print(l)
        return l
