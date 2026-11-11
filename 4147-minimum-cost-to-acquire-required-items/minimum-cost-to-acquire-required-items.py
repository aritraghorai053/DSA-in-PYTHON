class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)

        cost = common * min(costBoth, cost1 + cost2)

        cost += (need1 - common) * min(cost1, costBoth)
        cost += (need2 - common) * min(cost2, costBoth)

        return cost
