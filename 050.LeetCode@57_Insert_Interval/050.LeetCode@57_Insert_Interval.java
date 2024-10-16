class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int newStart = newInterval[0];
        int newEnd = newInterval[1];
        int i = 0;
        int n = intervals.length;
        List<int[]> output = new ArrayList<>();
        while (i < n && newStart > intervals[i][0]) {
            output.add(intervals[i]);
            i++;
        }
        if (output.isEmpty() || output.get(output.size() - 1)[1] < newStart) {
            output.add(newInterval);
        } else {
            output.get(output.size() - 1)[1] = Math.max(output.get(output.size() - 1)[1], newEnd);
        }
        while (i < n) {
            int start = intervals[i][0];
            int end = intervals[i][1];

            if (output.get(output.size() - 1)[1] < start) {
                output.add(intervals[i]);
            } else {
                output.get(output.size() - 1)[1] = Math.max(output.get(output.size() - 1)[1], end);
            }
            i++;
        }
        return output.toArray(new int[output.size()][]);
    }
}