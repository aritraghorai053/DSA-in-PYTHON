
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        freq = [0] * 26

        for ch in chars:
            freq[ord(ch) - 97] += 1

        total = 0

        for word in words:
            temp = freq.copy()

            for ch in word:
                idx = ord(ch) - 97
                temp[idx] -= 1

                if temp[idx] < 0:
                    break
            else:
                total += len(word)

        return total
