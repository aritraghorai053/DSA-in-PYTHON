
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):

            # Release completed servers
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                available.add(server)

            # No server available
            if not available:
                continue

            # Preferred server
            idx = i % k

            # Find next available server
            pos = available.bisect_left(idx)

            if pos == len(available):
                pos = 0

            server = available.pop(pos)

            # Update request count
            count[server] += 1

            # Mark server as busy
            heapq.heappush(busy, (arrival[i] + load[i], server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
