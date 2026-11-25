class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(0, n, 2):
            if nums[i] % 2 != 0:
                for j in range(1, n, 2):
                    if nums[j] % 2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

        return nums