
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        gain = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                gain[i] += freq[j]

            if freq[i] > 0:
                gain[i] -= 1

        deals = []

        for factor, price in items:
            if gain[factor] > 0 and price < 2 * min_price:
                deals.append((price, gain[factor]))

        deals.sort()

        ans = 0

        for price, count in deals:
            buy = min(count, budget // price)

            ans += buy * 2
            budget -= buy * price

        ans += budget // min_price

        return ans
