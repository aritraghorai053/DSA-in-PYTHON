class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        available = []
        busy = []

        # Store (weight, index) in available heap
        for i, weight in enumerate(servers):
            heapq.heappush(available, (weight, i))

        ans = []
        time = 0

        for i, task in enumerate(tasks):

            time = max(time, i)

            # Move completed servers to available heap
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If no server is available, wait
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select the best available server
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Mark server as busy
            heapq.heappush(busy, (time + task, weight, index))

        return ans
