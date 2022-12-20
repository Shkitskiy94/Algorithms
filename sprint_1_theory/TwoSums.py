from typing import List


class Solution:
    nums: List[int]
    target: int

    def __init__(self, nums: List[int], target: int):
        self.nums: List[int] = nums
        self.target: int = target

    def two_sum(self) -> List[int]:
        for first in range(len(self.nums)):
            for second in range(first+1, len(self.nums)):
                if self.nums[first] + self.nums[second] == self.target:
                    return [first, second]
            else:
                print('values error')

    def show_two_sum(self):
        return print(self.two_sum())


a = [1, 2, 3, 4]
b = 5

Solution(a, b).show_two_sum()

print(range(4))
