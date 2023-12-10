# You are given a 0-indexed array nums consisting of positive integers.
# A partition of an array into one or more contiguous subarrays is called good if no two 
# subarrays contain the same number.
# Return the total number of good partitions of nums.
# Since the answer may be large, return it modulo 10^9 + 7.

# Input: nums = [1,2,3,4]
# Output: 8
# Explanation: The 8 possible good partitions are: ([1], [2], [3], [4]), ([1], [2], [3,4]), 
# ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]), and 
# ([1,2,3,4]).
# Input: nums = [1,1,1,1]
# Output: 1
# Explanation: The only possible good partition is: ([1,1,1,1]).

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9

class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        last = {a: i for i,a in enumerate(nums)}
        res = 1
        mod = 10 ** 9 + 7
        j = 0
        for i,a in enumerate(nums):
            # a distinct subarray start
            if i > j:
                res = res * 2 % mod
            j = max(j, last[a])
        return res