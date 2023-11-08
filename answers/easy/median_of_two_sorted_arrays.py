from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    total_length = len(nums1) + len(nums2)
    if total_length == 0:
        return 0

    if total_length % 2 == 1:
        return find_kth_element(nums1, nums2, total_length // 2 + 1)
    else:
        return (find_kth_element(nums1, nums2, total_length // 2) + find_kth_element(nums1, nums2, total_length // 2 + 1)) / 2


def find_kth_element(num1: List[int], num2: List[int], k: int) -> int:
    length1 = len(num1)
    length2 = len(num2)
    index1 = index2 = 0

    while True:
        if index1 == length1:
            return num2[index2 + k - 1]
        elif index2 == length2:
            return num1[index1 + k - 1]

        if k == 1:
            return min(num1[index1], num2[index2])

        half = k // 2
        new_index_1 = min(index1 + half - 1, length1 - 1)
        new_index_2 = min(index2 + half - 1, length2 - 1)
        new_number_1 = num1[new_index_1]
        new_number_2 = num2[new_index_2]

        if new_number_1 <= new_number_2:
            k = k - (new_index_1 - index1 + 1)
            index1 = new_index_1 + 1
        else:
            k = k - (new_index_2 - index2 + 1)
            index2 = new_index_2 + 1
