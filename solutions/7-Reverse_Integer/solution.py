'''
7 - Reverse Integer

By Joseph Haenel

Difficulty: Medium

Time and Space Complexity: O(N)

No clue if this is optimal, just my solution I came up with from messing around
'''

class Solution:
    def reverse(self, x: int) -> int:
        maxValue = pow(2, 31) - 1
        minValue = pow(-2, 31)
        negative = False
        rVal = ""
        if x < 0:
            negative = True
            x = x * -1
        for i in range(1, len(str(x)) + 1):
            modVal = pow(10, i)
            val = x % modVal
            x = x - val
            val = str(val)[0]
            rVal += str(val)
            if int(rVal) > maxValue or int(rVal) < minValue:
                return 0
        if negative:
            rVal = '-' + rVal
        return int(rVal)

        