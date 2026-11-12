class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common = Counter(words[0])

        for word in words[1:]:
            freq = Counter(word)
            common &= freq

        result = []

        for char, count in common.items():
            result.extend([char] * count)

        return result