from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    candidates = {}

    for index, num in enumerate(nums):
        want = target - num
        if want in candidates:
            return [index, candidates[want]]
        candidates[num] = index

    return []
