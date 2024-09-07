class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        for(int i=citations.length-1;i>=0;i--){
            if (citations[i] < citations.length-i-1+1){
                return citations.length-i-1;
            }
        }
        return citations.length;
    }
}