class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        mid = len(nums) // 2
        median = nums[mid]

        moves = 0
        for num in nums:
            moves += abs(num - median)

        return moves