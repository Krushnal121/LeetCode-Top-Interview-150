class Solution:
    def search(self, nums, target):
        return self.search2(nums, 0, len(nums) - 1, target)

    def search2(self, arr, start, end, target):
        if start > end:
            return -1

        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid

        # Left half is sorted
        if arr[start] <= arr[mid]:
            if arr[start] <= target <= arr[mid]:
                return self.search2(arr, start, mid - 1, target)
            else:
                return self.search2(arr, mid + 1, end, target)

        # Right half is sorted
        else:
            if arr[mid] <= target <= arr[end]:
                return self.search2(arr, mid + 1, end, target)
            else:
                return self.search2(arr, start, mid - 1, target)
