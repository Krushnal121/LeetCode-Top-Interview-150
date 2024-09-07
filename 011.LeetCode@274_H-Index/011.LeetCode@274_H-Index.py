class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        length = len(citations)
        for i in range(length):
            if citations[i] < i + 1:
                return i
        return length