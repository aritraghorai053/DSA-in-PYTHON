class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            result = 0

            while num > 0:
                ld = num % 10
                result = result + ld
                num = num // 10

            num = result 
        return num