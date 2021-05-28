def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    candidates = {}

    for index, num in enumerate(nums):
        want = target - num
        if want in candidates:
            return [index, candidates[want]]
        candidates[num] = index

    return []
