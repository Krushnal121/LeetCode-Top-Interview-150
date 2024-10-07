class Solution {
    public boolean wordPattern(String pattern, String s) {
        String arr[] = s.split(" ");
        if (pattern.length() != arr.length)
            return false;
        HashMap<Character, String> h = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            if (!h.containsKey(pattern.charAt(i))) {
                if (!h.containsValue(arr[i])) {
                    h.put(pattern.charAt(i), arr[i]);
                } else return false;
            } else {
                if (arr[i].compareTo(h.get(pattern.charAt(i))) != 0) return false;
            }
        }
        return true;
    }
}