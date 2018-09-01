class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Largest,Second,myIndex = -1,-1,-i
        for i in range(len(nums)):
            if nums[i] > Largest:
                Second = Largest
                Largest = nums[i]
                myIndex = i
            elif nums[i] > Second:
                Second = nums[2]
        if Largest >= Second + Second:
            return myIndex
        else:
            return -1

