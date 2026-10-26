"""
LeetCode 1 - Two Sum
https://leetcode.com/problems/two-sum/

Estructura de datos: Hash Table (dict de Python).

Idea: se recorre el arreglo una sola vez guardando en un diccionario
{valor: indice}. Para cada numero se busca si su complemento
(target - num) ya fue visto; si esta, se devuelven ambos indices.

Complejidad: tiempo O(n), espacio O(n).
"""
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(s.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(s.twoSum([3, 3], 6)) == [0, 1]
    assert sorted(s.twoSum([-1, -2, -3, -4, -5], -8)) == [2, 4]
    print("two_sum: todos los tests pasaron")
