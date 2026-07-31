1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heap = []
4        for num in nums:
5            heapq.heappush(heap , num)
6            if len(heap) > k:
7                heapq.heappop(heap)
8
9        return heap[0]
10        