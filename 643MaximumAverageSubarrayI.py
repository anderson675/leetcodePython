class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = 0;
        sums = sum(nums[:k])
        res = sums
        for i in range(k,len(nums)):
            sums += (nums[i]- nums[i-k])
            if res < sums:
                res = sums;
        return res/k