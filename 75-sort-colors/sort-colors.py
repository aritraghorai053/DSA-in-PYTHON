class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)

        for i in range(n - 2, -1, -1):
            isSwap = False
            for j in range(0, i+1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    isSwap = True

            if isSwap == False:
                break