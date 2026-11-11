
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for s in strs:
            freq = {}

            for ch in s:
                freq[ch] = freq.get(ch, 0) + 1

            key = tuple(sorted(freq.items()))

            if key not in mp:
                mp[key] = []

            mp[key].append(s)

        return list(mp.values())
