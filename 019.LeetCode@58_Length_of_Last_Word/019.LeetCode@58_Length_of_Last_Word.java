class Solution {
    public int lengthOfLastWord(String s) {
        int i =s.length()-1;
        while(s.charAt(i)==' '){
            i--;
        }
        int x = i;
        while(x>=0 && s.charAt(x)!=' '){
            x--;
        }
        return i-x;
    }
}