class NumArray:
    def __init__(self, nums):
        # make empty prefix list
        self.prefix = [0] * len(nums)
        #initialize first element of prefix
        self.prefix[0] = nums[0]
        for i in range(1, len(nums)):
            # build prefix using the nums list element
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]
