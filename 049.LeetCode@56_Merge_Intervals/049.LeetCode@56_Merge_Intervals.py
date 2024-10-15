class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        start = intervals[0][0]
        end = intervals[0][1]
        ans=[]
        for i in range(1,len(intervals)):
            if intervals[i][0] > end:
                ans.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end =max(intervals[i][1],end)
        ans.append([start, end])
        return ans