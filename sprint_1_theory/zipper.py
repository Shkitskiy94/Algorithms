from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    return [item for sublist in zip(a, b) for item in sublist]


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))

# a = [1, 2, 3]
# b = [4, 5, 6]
#
# print(zipper(a, b))

