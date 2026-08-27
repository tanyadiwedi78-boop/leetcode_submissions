1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        i = m-1
4        j = n-1
5        k = m+n-1
6        while j >= 0:
7            if i >= 0 and nums1[i] > nums2[j]:
8                nums1[k] = nums1[i]
9                i -= 1
10            else:
11                nums1[k] = nums2[j]
12                j -= 1
13            k -= 1
14
15
16        