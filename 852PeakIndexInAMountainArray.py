class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        low = 0
        high = len(A)-1
        mid = 0
        while low < high:
            mid = low + (high - low)/2
            if A[mid]>A[mid-1]:
                high = mid
            else: 
                low = mid + 1
        return low