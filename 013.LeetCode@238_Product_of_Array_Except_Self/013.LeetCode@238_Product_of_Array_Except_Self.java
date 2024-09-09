class Solution {
    public int[] productExceptSelf(int[] nums) {
        int product = 1, cnt = 0;
        boolean iszero = false;
        for (int num : nums) {
            if (num == 0) {
                iszero = true;
                cnt++;
            } else {
                product *= num;
            }
        }
        if (iszero) {
            if (cnt > 1) {
                for (int i = 0; i < nums.length; i++) {
                    nums[i] = 0;
                }
                return nums;
            } else {
                for (int i = 0; i < nums.length; i++) {
                    if (nums[i] == 0) {
                        nums[i] = product;
                    } else {
                        nums[i] *= 0;
                    }
                }
                return nums;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            nums[i] = product / nums[i];
        }
        return nums;
    }
}