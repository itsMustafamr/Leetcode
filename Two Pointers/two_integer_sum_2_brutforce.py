from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #way 1 - brut force - o(n^2)
        for i in range(len(numbers)):
            for j in range(i + 1 , len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1,j + 1]