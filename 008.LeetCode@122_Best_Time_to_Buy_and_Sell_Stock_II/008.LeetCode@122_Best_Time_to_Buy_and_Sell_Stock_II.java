class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int start = prices[0];
        for(int price:prices){
            if(start < price) max += price - start;
            start = price;
        }
        return max;
    }
}