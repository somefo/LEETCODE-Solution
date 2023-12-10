# You are given a 0-indexed 2D array variables where variables[i] = [ai, bi, ci, mi], and an 
# integer target.

# An index i is good if the following formula holds:

#     0 <= i < variables.length
#     ((ai^bi % 10)^ci) % mi == target
# Return an array consisting of good indices in any order.

# Input: variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2
# Output: [0,2]
# Explanation: For each index i in the variables array:
# 1) For the index 0, variables[0] = [2,3,3,10], (2^3 % 10)^3 % 10 = 2.
# 2) For the index 1, variables[1] = [3,3,3,1], (3^3 % 10)^3 % 1 = 0.
# 3) For the index 2, variables[2] = [6,1,1,4], (6^1 % 10)^1 % 4 = 2.
# Therefore we return [0,2] as the answer.

# Constraints:

# 1 <= variables.length <= 100
# variables[i] == [ai, bi, ci, mi]
# 1 <= ai, bi, ci, mi <= 10^3
# 0 <= target <= 10^3

class Solution:
    def __init__(self) -> None:
        self.exp_mapping_table = {0:[0], 1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5],
                                  6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}

    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        good_index = []
        for i in range(len(variables)):
            a, b, c, m = variables[i]
            if m <= target:
                continue

            a0 = a % 10
            array_length = len(self.exp_mapping_table[a0])
            a_b = self.exp_mapping_table[a0][b % array_length - 1]
            
            temp_mapping = [a_b % m]
            last_element = a_b
            zero_flag = False
            while last_element * a_b % m not in temp_mapping :
                temp_mapping.append(last_element * a_b % m)
                last_element = last_element * a_b % m
                if last_element == 0:
                    zero_flag = True
            
            if zero_flag is False:
                a_b_c_m = temp_mapping[c % len(temp_mapping) -1]
            else:
                if c > len(temp_mapping) - 1:
                    a_b_c_m = 0
                else:
                    a_b_c_m = temp_mapping[c - 1]
            if a_b_c_m == target:
                good_index.append(i)

        return good_index



