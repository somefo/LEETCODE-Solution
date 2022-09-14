# Code solution for leetcode


class Solution:
    def run(self, height):
        max_area = 0

        # recursive
        def Maxarea(left, right):
            if right - left == 1:
                return min(height[left], height[right])

            area = min(height[left], height[right]) * (right - left)
            if height[left] < height[right]:
                return max(area, Maxarea(left + 1, right))

            if height[left] >= height[right]:
                return max(area, Maxarea(left, right - 1))

        # non-recursive
        i, j = 0, len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if max_area < area:
                max_area = area

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return Maxarea(0, len(height) - 1)  # max_area


if __name__ == '__main__':
    print(Solution().run([1,8,6,2,5,4,8,3,7]))
    print(Solution().run([1,1]))