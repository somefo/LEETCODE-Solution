# You are given an integer array nums and a positive integer k.
# Return the number of subarrays where the maximum element of nums appears at least k times in 
# that subarray.
# A subarray is a contiguous sequence of elements within an array.

# Input: nums = [1,3,2,3,3], k = 2
# Output: 6
# Explanation: The subarrays that contain the element 3 at least 2 times are: 
# [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

# Input: nums = [1,4,2,1], k = 3
# Output: 0
# Explanation: No subarray contains the element 4 at least 3 times.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= 10^5
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # O(n^2) time complexity, O(1) space complexity
        # Time Limit Exceed
        max_num = 0
        count = 0 # total count of max number
        for number in nums:
            if number > max_num:
                max_num = number
                count = 1
            elif number == max_num:
                count += 1
        
        sub_count = 0 # total count of subarray
        
        for tail in range(len(nums)-1, -1, -1):
            if tail != len(nums) - 1 and nums[tail + 1] == max_num:
                count -= 1
            # break loop when [0, tail] subarray has at most k - 1 max_num.
            if count < k:
                break
            temp_count = 0
            for head in range(tail, -1, -1):
                if nums[head] == max_num:
                    temp_count += 1
                # break loop when [head, tail] subarray has at most k - 1 max_num.
                if temp_count >= k:
                    sub_count += head + 1
                    break
                
        return sub_count
    
    def countSubarrays2(self, nums: List[int], k: int) -> int:
        # Time Limit Exceed
        max_num_index = []
        max_num = 0
        for num in nums:
            if num > max_num :
                max_num = num

        for i,num in enumerate(nums):
            if num == max_num:
                max_num_index.append(i)
        
        if len(max_num_index) < k:
            return 0
        
        count = 0
        window_size = k
        while window_size <= len(max_num_index):
            for i in range(0, len(max_num_index) - window_size + 1):
                front, end = max_num_index[i], max_num_index[i + window_size - 1]
                before_interval = front - (-1) if i == 0 else front - max_num_index[i-1]
                after_interval = len(nums) - end if i + window_size == len(max_num_index) else max_num_index[i + window_size] - end
                count += before_interval * after_interval
            
            window_size += 1
        return count
    
    def countSubarray3(self, nums: List[int], k: int) -> int:
        # O(n) time complexity
        res = 0
        max_num = 0
        count = 0
        for num in nums:
            if num > max_num:
                max_num = num
                count = 1
            elif num == max_num:
                count += 1
        
        if count < k:
            return 0
        max_num_index = [index for index, val in enumerate(nums) if val == max_num]
        last_index = len(nums)
        for i,index in enumerate(max_num_index):
            if i + k > len(max_num_index):
                break
            
            pre_index = -1 if i == 0 else max_num_index[i-1]
            res += (index - pre_index) * (last_index - max_num_index[i + k -1])
        
        return res

    
def test(f:Solution):
    nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
    k = 2
    print(f.countSubarrays(nums, k))
    print(f.countSubarrays2(nums, k))
    print(f.countSubarray3(nums, k))
    nums = [1, 4, 5, 3, 4, 5, 1]
    k = 2
    print(f.countSubarrays(nums, k))
    print(f.countSubarrays2(nums, k))
    print(f.countSubarray3(nums, k))

if __name__ == '__main__':
    F = Solution()
    test(F)