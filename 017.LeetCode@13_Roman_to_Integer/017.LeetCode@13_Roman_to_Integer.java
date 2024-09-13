class Solution {
    public int romanToInt(String s) {
        HashMap<String, Integer> roman = new HashMap<>();
        roman.put("I", 1);
        roman.put("V", 5);
        roman.put("X", 10);
        roman.put("L", 50);
        roman.put("C", 100);
        roman.put("D", 500);
        roman.put("M", 1000);
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i + 1 < s.length() && roman.get(s.substring(i, i + 1)) < roman.get(s.substring(i + 1, i + 2))) {
                res -= roman.get(s.substring(i, i + 1));
            } else {
                res += roman.get(s.substring(i, i + 1));
            }
        }
        return res;
    }
}