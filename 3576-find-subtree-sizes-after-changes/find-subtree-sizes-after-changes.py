
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]
            old = last.get(ch, -1)

            if old != -1:
                new_parent[node] = old

            last[ch] = node

            for child in children[node]:
                dfs(child)

            if old == -1:
                last.pop(ch)
            else:
                last[ch] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        ans = [0] * n

        def calculate(node):
            size = 1

            for child in new_children[node]:
                size += calculate(child)

            ans[node] = size
            return size

        calculate(0)

        return ans
