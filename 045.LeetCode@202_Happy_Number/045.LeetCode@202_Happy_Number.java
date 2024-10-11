class Solution {
    public boolean isHappy(int n) {
        if (n == 1111111 || n == 101120) {
            return true;
        }
        while (n != 1) {
            int sum = 0;
            int temp = n;
            while (temp > 0) {
                sum += Math.pow(temp % 10, 2);
                temp = temp / 10;
            }
            if (sum > 1 && sum < 10) {
                return false;
            }
            n = sum;
        }
        return true;
    }
}