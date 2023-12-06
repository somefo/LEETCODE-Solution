# Description: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Input: nums = [0,1,1]
# Output: []
def quicksort(nums: List[int], l:int, r:int) -> int:
    if l >= r:
        return 0
    old_l = l
    old_r = r
    pivot = nums[l] 
    # update element one by one, do not swap directly
    while l < r:
        while nums[r] >= pivot and r > l :
            r -= 1
        nums[l] = nums[r]

        while nums[l] <= pivot and l < r:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    quicksort(nums, old_l, l - 1)
    quicksort(nums, l + 1, old_r)
    return 0

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        right = len(nums) - 1
        result = []
        quicksort(nums, left, right)
        
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: # skip duplicate but allow first duplicate elements
                continue

            sum = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + sum > 0:
                    right -= 1
                
                elif nums[left] + nums[right] + sum < 0:
                    left += 1
                
                else:
                    # skip duplicate
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1

        return result