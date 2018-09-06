class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        first, left, maxLen = -1, -1, 0
        for i in range(len(seats)):
            if seats[i] == 1:
                if left == -1:
                    first = i
                    left = i
                else:
                    maxLen = max(maxLen, (i - left) // 2)
                    left = i
        return max(first, max(maxLen, len(seats) - 1 - left))