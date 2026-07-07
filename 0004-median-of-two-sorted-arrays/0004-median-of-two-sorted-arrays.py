from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search hamesha choti array par lagao
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = m + n
        half = (total + 1) // 2

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2   # nums1 ka cut
            j = half - i              # nums2 ka cut

            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < m else float("inf")

            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < n else float("inf")

            # correct partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # odd length
                if total % 2 == 1:
                    return float(max(nums1_left, nums2_left))

                # even length
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            # nums1 ka left part zyada bara hai
            elif nums1_left > nums2_right:
                right = i - 1

            # nums1 ka left part chota hai
            else:
                left = i + 1