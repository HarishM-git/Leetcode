class Solution:
    def strStr(self, ha: str, co: str) -> int:
        
        
        for j in range(len(ha)):
            if(co[0]==ha[j]):
                # print(co[0:],"ha",ha[j:len(co)])
                if(co[0:]==ha[j:j+len(co)]):
                    return(j)
        return(-1)
                
 
