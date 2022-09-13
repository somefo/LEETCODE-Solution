# Code solution for leetcode
# Time 2022-09-12
import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a
        total = len(a) + len(b)
        half = total // 2
        l = 0
        r = len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            aleft = a[i] if i >= 0 else - math.pow(10,7)
            aright = a[i + 1] if i + 1 < len(a) else math.pow(10,7)
            bleft = b[j] if j >= 0 else - math.pow(10,7)
            bright = b[j + 1] if j + 1 < len(b) else math.pow(10,7)

            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))