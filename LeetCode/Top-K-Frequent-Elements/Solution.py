1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freq  = Counter(nums)
4        heap = []
5        for num , count in freq.items():
6            heapq.heappush(heap ,(count , num) )
7            if len(heap) > k:
8                heapq.heappop(heap)
9        return [num for count , num in heap]
10
11        # time complexity -> 
12        # counting frequencies: O(n)
13        # Heap operations :  O(m log k) , where m is the no. of unique elements
14        # Overall : O(n log k)
15        