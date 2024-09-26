import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=currentsum=0
        minlength=len(nums)+1
        for right in range (len(nums)):
            currentsum+=nums[right]
            while(currentsum>=target):
                minlength=min(minlength,right-left+1)
                currentsum-=nums[left]
                left+=1
        return 0 if minlength==len(nums)+1 else minlength