class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        sorted_chars = sorted(freq, key=lambda ch: freq[ch], reverse=True)

        result = ""

        for ch in sorted_chars:
            result += ch * freq[ch]

        return result
