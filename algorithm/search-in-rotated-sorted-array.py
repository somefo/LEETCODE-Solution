#Code Solution for Leetcode problem 33
#https://leetcode.com/problems/search-in-rotated-sorted-array/


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        def binary_search(l, r, target):
            mid = (l + r) // 2
            flag = -1
            while nums[mid] != target:
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid
                mid = (l + r) // 2
                if r - l <= 1:
                    if nums[r] == target:
                        flag = r
                    if nums[l] == target:
                        flag = l
                    break
            if nums[mid] == target:
                flag = mid
            return flag

        # No rotation
        if nums[left] < nums[right]:
            index = binary_search(left, right, target)
            return index

        middle = (left + right) // 2
        while middle > left:
            a = nums[middle]
            if a > nums[right]:
                left = middle
            else:
                right = middle

            middle = (left + right) // 2

        if target < nums[0]:
            left, right = right, len(nums) - 1
        else:
            left, right = 0, left
        # print(left, right)
        index = binary_search(left, right, target)
        return index


if __name__ == '__main__':
    nums = [[4, 5, 6, 7, 0, 1, 2],[4, 5, 6, 7, 0, 1, 2],[1]]
    target = [0, 3, 0]
    for i, num in enumerate(nums):
        print(Solution().search(num, target[i]))

