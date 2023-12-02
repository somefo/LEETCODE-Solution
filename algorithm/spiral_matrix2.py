# Descriptipn: Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
# Constraints: 1 <= n <= 20
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
# Input: n = 1
# Output: [[1]]

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        orientation = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        border = [n, n, -1, 0]
        x, y = 0, 0
        direction = 0
        ret = [[0] * n for i in range(n)]
        for i in range(0, n*n):
            ret[y][x] = i + 1
            # current direction
            next_move = orientation[direction % 4]
            # judge if need to change direction
            if (x + next_move[0] == border[direction % 4] and next_move[0] != 0) or \
            (y + next_move[1] == border[direction % 4] and next_move[1] != 0):
                # change border according to moving direction
                border[direction % 4] -= next_move[0] + next_move[1]  
                direction += 1
            update_move = orientation[direction % 4]
            x += update_move[0]
            y += update_move[1]

        return ret
