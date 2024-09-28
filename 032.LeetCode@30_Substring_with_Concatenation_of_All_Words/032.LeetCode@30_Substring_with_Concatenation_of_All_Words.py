class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        n = len(s)
        m = len(words)
        w = len(words[0])
        hm = {}
        for x in words:
            hm[x] = hm.get(x, 0) + 1
        for i in range(w):
            temp = {}
            count = 0
            j = k = i
            for j in range(i, n - w + 1, w):
                word = s[j:j + w]
                temp[word] = temp.get(word, 0) + 1
                count += 1

                if count == m:
                    if hm == temp:
                        ans.append(k)
                    remove = s[k:k + w]
                    if remove in temp:
                        temp[remove] = temp[remove] - 1 if temp[remove] > 1 else None
                        if temp[remove] is None:
                            del temp[remove]
                    count -= 1
                    k = k + w
        return ans