class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq = {}

        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        result = []

        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]

        for num in sorted(freq):
            result.extend([num] * freq[num])

        return result
