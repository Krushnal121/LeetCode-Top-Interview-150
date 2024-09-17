class Solution {
    public String reverseWords(String s) {
        String[] str = s.trim().split("\\s+");
        StringBuilder out = new StringBuilder();
        for (int i = str.length - 1; i > 0; i--) {
            out.append(str[i]).append(" ");
        }
        return out.append(str[0]).toString();
    }
}