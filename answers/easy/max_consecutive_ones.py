def find_max_consecutive_ones(nums):
    result = 0
    length = 0

    for n in nums:
        if n == 1:
            length = length + 1
            if length > result:
                result = length
        else:
            length = 0

    return result
