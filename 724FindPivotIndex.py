class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            total -= nums[i]
            if(total == lsum):
                return i
            lsum += nums[i]
        return -1