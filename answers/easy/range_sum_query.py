class RangeSumQuery:
    def __init__(self, nums):
        self.accSum = [0 for _ in range(len(nums))]
        self.accSum[0] = nums[0]
        for i in range(1, len(nums)):
            self.accSum[i] = self.accSum[i - 1] + nums[i]

    def sum_range(self, left, right):
        return self.accSum[right] - (0 if left == 0 else self.accSum[left - 1])
