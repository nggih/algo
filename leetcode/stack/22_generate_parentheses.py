from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parentheses if open < n
        # only add a closing p if closed < open
        # valid iif open == closed == n

        stack = []
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()
            
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()
        
        backtrack(0,0)
        return res