
class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        rev = 0

        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num = num // 10

        if x < 0:
            rev = -rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev
