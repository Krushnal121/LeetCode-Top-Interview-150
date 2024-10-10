class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                idx=nums[i+1:].index(target-nums[i])+i+1
            except:
                continue
            if (target-nums[i])in nums and idx!=i:
                return [i,idx]
            else:continue