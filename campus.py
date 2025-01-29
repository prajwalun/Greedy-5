# The assignBikes method assigns bikes to workers based on the shortest Manhattan distance.

# Approach:
# - Compute and store all distances between workers and bikes in a min-heap.
# - Use a priority queue to assign the closest available bike to each worker.
# - If a bike is already taken, fetch the next closest bike for that worker.

# TC: O(m * n log n) - Sorting and heap operations per worker.
# SC: O(m * n) - Space for storing distances.


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distance = []
        for i, w in enumerate(workers):
            distance.append([])
            for j, b in enumerate(bikes):
                distance[-1].append([abs(w[0]-b[0]) + abs(w[1]-b[1]), i, j])
            heapq.heapify(distance[-1])
        ans = [-1] * len(workers)
        used_bikes = set()
        heap = [heapq.heappop(d) for d in distance]
        heapq.heapify(heap)
        while len(used_bikes) < len(workers):
            _, w, b = heapq.heappop(heap)
            if b in used_bikes:
                heapq.heappush(heap, heapq.heappop(distance[w]))
            else:
                used_bikes.add(b)
                ans[w] = b
        return ans 