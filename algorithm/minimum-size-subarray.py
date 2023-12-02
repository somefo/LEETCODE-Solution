# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# Constraints:

# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum_length = 100001
        i, j = 0, 0
        array_length = len(nums)
        sub_sum = nums[i]
        while 1: # sliding window
            if sub_sum >= target:
                minimum_length = min(minimum_length, j - i + 1)
                if minimum_length == 1:
                    return 1
                # narrow down left window
                sub_sum -= nums[i]
                i += 1
            else:
                # expand right window
                j += 1
                if j == array_length:
                    break
                sub_sum += nums[j]
        if minimum_length == 100001:
            return 0
        return minimum_length

