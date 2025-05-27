class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):

                if nums[i]+nums[j]==target:
                    h.append(i)
                    h.append(j)
                    return h
