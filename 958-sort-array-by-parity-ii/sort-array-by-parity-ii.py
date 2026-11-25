class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        size = len(nums)
        even, odd = 0,1
        while even<size-1 and odd<size:
            if nums[even]%2==0:
                even += 2
            elif nums[odd]%2==1:
                odd += 2
            else:
                nums[odd], nums[even] = nums[even], nums[odd]
                even += 2
                odd += 2
        
        return nums
        