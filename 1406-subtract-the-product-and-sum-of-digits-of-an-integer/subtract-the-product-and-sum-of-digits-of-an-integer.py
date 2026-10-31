class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = n 
        pod = 1
        sod = 0
        while num > 0:
            ld = num % 10
            pod = pod * ld
            sod = sod + ld
            num = num // 10

        result = pod - sod
        return result