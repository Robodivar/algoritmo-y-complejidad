"""
LeetCode 215 - Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Estructura de datos: Priority Queue (min-heap con heapq).

Idea: se mantiene un min-heap con a lo sumo k elementos. Si el heap crece
por encima de k, se elimina el minimo. Al final, la raiz del heap es el
k-esimo elemento mas grande.

Complejidad: tiempo O(n log k), espacio O(k).
"""
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


if __name__ == "__main__":
    s = Solution()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([1], 1) == 1
    assert s.findKthLargest([-1, -1], 2) == -1
    print("kth_largest: todos los tests pasaron")
