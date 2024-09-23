class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int startidx=0, endidx=numbers.length-1;
        while(startidx<endidx){
            int sum=numbers[startidx]+numbers[endidx];
            if(sum==target){
                return new int[]{startidx+1, endidx+1};
            }
            else if(sum>target){
                endidx--;
            }
            else{
                startidx++;
            }
        }
        return new int[]{-1,-1};
    }
}