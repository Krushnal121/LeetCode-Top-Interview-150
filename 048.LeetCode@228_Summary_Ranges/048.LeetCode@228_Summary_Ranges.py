class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []
        if n == 0:
            return ans
        start = 0
        for end in range(1, len(nums) + 1):
            if end == n or nums[end - 1] + 1 != nums[end]:
                if start == end - 1:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + '->' + str(nums[end - 1]))
                start = end
        return ans