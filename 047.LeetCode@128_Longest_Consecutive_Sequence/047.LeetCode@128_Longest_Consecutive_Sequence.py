class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:return 0
        nums.sort()
        length = maxlength =1
        for i in range (1,len(nums)):
            if nums[i] == nums[i-1]+1:
                length+=1
                maxlength = max(maxlength,length)
            elif nums[i] == nums[i-1]:
                continue
            else:
                length = 1
        return maxlength