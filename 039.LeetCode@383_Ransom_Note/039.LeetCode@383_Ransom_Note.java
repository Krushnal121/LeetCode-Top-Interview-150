class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        int[] letters = new int[26];
        for (char c : ransomNote.toCharArray()) {
            int i = magazine.indexOf(c, letters[c % 26]);
            if (i == -1) return false;
            letters[c % 26] = i + 1;
        }
        return true;
    }
}