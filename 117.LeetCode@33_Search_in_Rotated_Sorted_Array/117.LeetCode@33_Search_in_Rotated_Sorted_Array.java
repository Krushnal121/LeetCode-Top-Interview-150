class Solution {
    public int search(int[] nums, int target) {
        return search2(nums, 0, nums.length - 1, target);
    }

    public int search2(int[] arr, int start, int end, int target) {
        if (start > end) {
            return -1;
        }

        int mid = start + (end - start) / 2;

        if (arr[mid] == target) {
            return mid;
        }

        if (arr[start] <= arr[mid]) {
            if (arr[start] <= target && target <= arr[mid]) {
                return search2(arr, start, mid - 1, target);
            } else {
                return search2(arr, mid + 1, end, target);
            }
        } else {
            if (arr[mid] <= target && target <= arr[end]) {
                return search2(arr, mid + 1, end, target);
            } else {
                return search2(arr, start, mid - 1, target);
            }
        }
    }
}