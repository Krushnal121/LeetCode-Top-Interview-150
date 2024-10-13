class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        Arrays.sort(nums);
        int length = 1, maxlength = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) continue;
            else if (nums[i] == nums[i - 1] + 1) {
                length++;
                maxlength = Math.max(length, maxlength);
            } else {
                length = 1;
            }
        }
        return maxlength;
    }
}