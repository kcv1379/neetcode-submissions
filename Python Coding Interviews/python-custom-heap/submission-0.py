import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    x = []
    y = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(x, pair)

    while x:
        y.append((heapq.heappop(x))[1])
    
    return y




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
