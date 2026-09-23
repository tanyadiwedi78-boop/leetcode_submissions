1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        m = len(nums1)
4        n = len(nums2)
5        if m > n:
6            nums1 , nums2 = nums2 , nums1
7            m , n = n , m # binary search on smaller array
8
9        left = 0
10        right = m
11        half = (m  + n  + 1) // 2
12        while left <= right:
13            i = (left + right) // 2
14            j = half - i
15            Aleft = float("-inf") if i == 0 else nums1[i - 1] # partition position of nums1 -> left
16            Aright = float("inf") if i == m else nums1[i] # partition position of nums1 -> right
17
18            Bleft = float("-inf") if j == 0 else nums2[j - 1] # # partition position of nums2 -> left
19            Bright = float("inf") if j == n else nums2[j] # # partition position of nums2 -> right
20
21                # correct partition
22            if Aleft <= Bright and Bleft <= Aright:
23
24                    # elements of aleft is smaleer than the a right
25
26                if (m + n) % 2 == 1:
27                        # odd total
28                    return max(Aleft , Bleft)
29
30                return (max(Aleft , Bleft) + min(Aright , Bright)) / 2
31
32            elif Aleft > Bright:
33                    right = i - 1
34            else:
35                    left = i + 1
36                        
37
38
39
40
41                
42        