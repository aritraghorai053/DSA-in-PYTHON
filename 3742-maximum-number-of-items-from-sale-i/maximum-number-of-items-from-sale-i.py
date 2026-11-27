
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Calculate free items for every item type
        bonus = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        # Group items by price
        groups = {}

        for i in range(n):
            factor, price = items[i]
            weight = 1 + bonus[i]

            if price not in groups:
                groups[price] = []

            groups[price].append(weight)

        # dp[c] = maximum bonus value with exact cost c
        dp = [-1] * (budget + 1)
        dp[0] = 0

        ans = 0

        # Process prices from expensive to cheap
        for price in sorted(groups, reverse=True):

            # Subsets containing at least one item of this price
            current = [-1] * (budget + 1)

            for weight in groups[price]:
                for b in range(budget, price - 1, -1):

                    if dp[b - price] != -1:
                        current[b] = max(
                            current[b],
                            dp[b - price] + weight
                        )

                    if current[b - price] != -1:
                        current[b] = max(
                            current[b],
                            current[b - price] + weight
                        )

            # Calculate maximum total items
            for b in range(budget + 1):
                if current[b] != -1:
                    extra = (budget - b) // price

                    ans = max(
                        ans,
                        current[b] + extra
                    )

            # Update DP for the next price group
            for weight in groups[price]:
                for b in range(budget, price - 1, -1):
                    if dp[b - price] != -1:
                        dp[b] = max(
                            dp[b],
                            dp[b - price] + weight
                        )

        return ans
