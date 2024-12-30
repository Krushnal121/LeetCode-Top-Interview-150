class MedianFinder:

    def __init__(self):
        # Min-heap for the larger half of the numbers
        self.minHeapForLargeNum = []
        # Max-heap for the smaller half of the numbers (invert numbers to use
        # heapq as a max-heap)
        self.maxHeapForSmallNum = []

    def addNum(self, num: int) -> None:
        if len(self.maxHeapForSmallNum) == 0 or -self.maxHeapForSmallNum[0] >= num:
            heapq.heappush(self.maxHeapForSmallNum, -num)
        else:
            heapq.heappush(self.minHeapForLargeNum, num)

        # Balance the heaps
        if len(self.maxHeapForSmallNum) > len(self.minHeapForLargeNum) + 1:
            heapq.heappush(
                self.minHeapForLargeNum, -heapq.heappop(self.maxHeapForSmallNum)
            )
        elif len(self.maxHeapForSmallNum) < len(self.minHeapForLargeNum):
            heapq.heappush(
                self.maxHeapForSmallNum, -heapq.heappop(self.minHeapForLargeNum)
            )

    def findMedian(self) -> float:
        if len(self.maxHeapForSmallNum) == len(self.minHeapForLargeNum):
            return (-self.maxHeapForSmallNum[0] + self.minHeapForLargeNum[0]) / 2.0
        else:
            return -self.maxHeapForSmallNum[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()