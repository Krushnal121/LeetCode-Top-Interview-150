class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length

        temp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = temp