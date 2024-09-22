class Solution {
    public boolean isSubsequence(String s, String t) {
        int stridx=0, subidx=0;
        while (stridx<t.length() && subidx<s.length()) {
            if (t.charAt(stridx) == s.charAt(subidx)) {
                stridx++;
                subidx++;
            }
            else {
                stridx++;
            }
        }
        return subidx==s.length();
    }
}