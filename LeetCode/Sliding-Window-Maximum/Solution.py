1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        dq = deque() # indices store
4        result = []
5
6        for i in range(len(nums)):
7            if dq and dq[0] < i - k + 1:
8                dq.popleft()
9
10            while dq and nums[dq[-1]] < nums[i]:
11                dq.pop()
12            
13            dq.append(i)
14            if i >= k - 1:
15                result.append(nums[dq[0]])
16        return result
17
18        