class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        freq = Counter(chars)
        total = 0

        for word in words:
            word_freq = Counter(word)

            for ch in word_freq:
                if word_freq[ch] > freq[ch]:
                    break
            else:
                    total += len(word)
        return total