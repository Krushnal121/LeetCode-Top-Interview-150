class Solution:
    def longestCommonPrefix(self, lst: List[str]) -> str:
        lst.sort()
        word = ""
        for i in range(min(len(lst[0]), len(lst[-1]))):
            if lst[0][i] != lst[-1][i]:
                return word
            else:
                word += lst[0][i]
        return word