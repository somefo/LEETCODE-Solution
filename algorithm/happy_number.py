# Description: Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
# Input: n = 19
# Output: true
# Input: n = 2
# Output: false

class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map = {}
        while 1:
            sum = 0
            while n != 0:
                digit = n % 10
                n = n // 10
                sum += digit * digit
            
            if sum == 1:
                return True
            if sum in hash_map.keys():
                return False
            
            hash_map[sum] = True
            n = sum