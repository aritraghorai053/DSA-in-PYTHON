
class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] ^= val
            i += i & -i

    def query(self, i):
        ans = 0
        while i:
            ans ^= self.tree[i]
            i -= i & -i
        return ans


class Solution:
    def palindromePath(self, n: int, edges: list[list[int]],
                       s: str, queries: list[str]) -> list[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        # Iterative DFS avoids recursion-depth errors
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = u if p == -1 else p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in graph[u]:
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        LOG = n.bit_length()
        up = [parent[:]]

        for j in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0

            while diff:
                if diff & 1:
                    u = up[j][u]
                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        bit = [1 << (ord(c) - ord('a')) for c in s]
        fenwick = BIT(n + 1)

        for u in range(n):
            fenwick.update(tin[u], bit[u])
            fenwick.update(tout[u], bit[u])

        ans = []

        for q in queries:
            op, a, b = q.split()
            u = int(a)

            if op == "update":
                new_bit = 1 << (ord(b) - ord('a'))
                delta = bit[u] ^ new_bit

                if delta:
                    fenwick.update(tin[u], delta)
                    fenwick.update(tout[u], delta)
                    bit[u] = new_bit

            else:
                v = int(b)
                w = lca(u, v)

                mask = (fenwick.query(tin[u] + 1)
                        ^ fenwick.query(tin[v] + 1)
                        ^ bit[w])

                ans.append((mask & (mask - 1)) == 0)

        return ans
