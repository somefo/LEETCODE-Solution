#Solution for Leetcode Problem
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        middle = (left + right) // 2
        while middle > left:
            a = nums[middle]
            if a > nums[right]:
                left = middle
            else:
                right = middle
            middle = (left + right) // 2
        return nums[right]