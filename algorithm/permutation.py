# Solution for Leetcode 46. Permutations

class Solution(object):
    def permute(self, nums):
        import copy
        if not nums:
            return []
        n = len(nums)
        permutations = []

        def backtrack(path, hashset):
            if len(path) == n:
                # list is a mutable object, so need to save its value copy but not itself
                permutations.append(copy.copy(path))
                return
            for num in nums:
                if num not in hashset:
                    path.append(num)
                    hashset.add(num)
                    backtrack(path, hashset)
                    path.pop()
                    hashset.remove(num)

        backtrack([], set())

        return permutations


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
