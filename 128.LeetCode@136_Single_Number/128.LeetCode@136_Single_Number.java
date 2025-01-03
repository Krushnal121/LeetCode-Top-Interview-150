public class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
            System.out.println(result);
        }
        return result;
    }
}