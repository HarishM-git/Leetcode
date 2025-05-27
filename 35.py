class Solution:
    def searchInsert(self, nums: List[int], t: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            m=(l+r)//2
            if(nums[m]==t):
                return m
            elif(nums[m]>t):
                r=m-1
            else:
                l=m+1
        return l
