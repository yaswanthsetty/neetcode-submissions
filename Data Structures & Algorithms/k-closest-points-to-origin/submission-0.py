class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = [(x*x+y*y,[x,y]) for x,y in points]
        heapq.heapify(x)
        return [heapq.heappop(x)[1] for _ in range(k)]