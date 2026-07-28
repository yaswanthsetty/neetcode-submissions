class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            f = heapq.heappop(stones)
            s = heapq.heappop(stones)   
            if f != s:
                heapq.heappush(stones,-abs(f-s))
        return abs(stones[0]) if len(stones) == 1 else 0