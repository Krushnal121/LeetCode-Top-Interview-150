class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || numRows >= s.length()) return s;
        StringBuilder[] sol = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            sol[i] = new StringBuilder();
        }
        int idx = 0, idxlst = 0, increment = 1;
        while (idx < s.length()) {
            while (idx < s.length() && idxlst < numRows && idxlst > -1) {
                sol[idxlst].append(s.charAt(idx));
                idx++;
                idxlst += increment;
            }
            increment *= -1;
            idxlst += increment;
            idxlst += increment;
        }
        for (int i = 1; i < numRows; i++) {
            sol[0].append(sol[i]);
        }
        return sol[0].toString();
    }
}