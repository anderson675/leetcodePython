class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        count = 0
        for num in nums:
            if num == 1:
                count+=1
                if max < count:
                    max = count
            else:
                count = 0;
        return max
