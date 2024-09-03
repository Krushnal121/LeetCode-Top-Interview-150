class Solution {
    public int maxProfit(int[] prices) {
        int prevlow=prices[0], max=0;
        for (int price:prices){
            prevlow=Math.min(price, prevlow);
            max=Math.max((price-prevlow),max);
        }
        return max;
    }
}