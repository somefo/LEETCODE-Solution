# Solution for leetcode

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        proirity = {'(': 2, '+': 1, '-': 1, ')': 0, ' ': 0}
        op_stack = []
        value_stack = []
        L = len(s)

        def calculate(op_stack, value_stack, index):
            flag = True
            while index < L:
                if s[index] not in proirity:
                    temp = ''
                    while s[index] not in proirity:
                        temp += s[index]
                        index += 1
                        if index >= L:
                            break
                    value_stack.append(int(temp))

                elif len(value_stack) == 0 and s[index] == '-':
                    index += 1
                    while s[index] == ' ':
                        index += 1
                    if s[index]>= '0' and s[index] <= '9':
                        temp = ''
                        while s[index] not in proirity:
                            temp += s[index]
                            index += 1
                            if index >= L:
                                break
                        value_stack.append(-int(temp))
                    else:
                        # (
                        flag = False

                else:
                    if s[index] == ' ':
                        index += 1
                        continue
                    if s[index] == ')':
                        index += 1
                        break

                    if s[index] == '+' or s[index] == '-':
                        op_stack.append(s[index])
                        index += 1
                    if s[index] == '(':
                        temp_value = []
                        temp_op = []
                        index, value = calculate(temp_op, temp_value, index + 1)
                        if flag is False:
                            value *= -1
                            flag = True
                        value_stack.append(value)

                if len(op_stack) > 0 and len(value_stack) > 1:
                    op = op_stack.pop()
                    if op == '+':
                        value_stack.append(value_stack.pop() + value_stack.pop())
                    elif op == '-':
                        value_stack.append(-value_stack.pop() + value_stack.pop())
            value = value_stack.pop()
            return index, value

        return calculate(op_stack, value_stack, 0)[1]

