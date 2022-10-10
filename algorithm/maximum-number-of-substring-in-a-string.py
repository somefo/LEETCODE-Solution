#Solution for Leetcode Problem
#https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/
#related topic: prefix sum, greedy

class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        value_order = []
        count_value = {}
        # using a dictionary to save count
        for char in pattern:
            count_value[char] = 0

        count = 0
        # extreme case: pattern[0] == pattern[1]
        if pattern[0] == pattern[1]:
            for char in text:
                if char == pattern[0]:
                    count_value[char] += 1
                    count += len(value_order)
                    value_order.append(char)
        else:
            for char in text:
                if char == pattern[0] or char == pattern[1]:
                    count_value[char] += 1
                    if char == pattern[0]:
                        value_order.append(char)
                    else:
                        count += len(value_order)

        count += max(count_value.values())
        return count
