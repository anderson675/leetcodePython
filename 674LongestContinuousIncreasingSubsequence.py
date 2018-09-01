class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        ret = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i]<=nums[i-1]:
                count = 1
            else: count +=1
            ret = max(ret, count)
        return ret