class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        b=1
        for i in range(len(s)-1,-1,-1):
            if(s[i]==' ') and b==1:
                continue
            elif(s[i]==' ') and b==0:
                break
            else:
                b=0
                c+=1
        return c
