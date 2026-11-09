class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        count = 0
        for ch in jewels:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in stones:
            if ch in freq:
                count += 1

        return count