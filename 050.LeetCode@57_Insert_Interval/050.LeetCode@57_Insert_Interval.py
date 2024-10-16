class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        newStart = newInterval[0]
        newEnd = newInterval[1]
        i = 0
        n = len(intervals)
        while i < n and newStart > intervals[i][0]:
            output.append(intervals[i])
            i += 1
        if not output or output[-1][1] < newStart:
            output.append(newInterval)
        else:
            output[-1][1] = max(output[-1][1], newEnd)
        while i < n:
            start, end = intervals[i]

            if output[-1][1] < start:
                output.append([start, end])
            else:
                output[-1][1] = max(output[-1][1], end)
            i += 1
        return output