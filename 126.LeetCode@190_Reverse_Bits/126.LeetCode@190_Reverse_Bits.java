public class Solution {
    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = res << 1;        // Shift res left
            res += (n & 1);        // Add the least significant bit of n to res
            n = n >> 1;            // Shift n to the right
        }
        return res;
    }
}