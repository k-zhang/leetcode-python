def remove_element(nums, val):
    p = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[p] = nums[i]
            p = p + 1

    return p
