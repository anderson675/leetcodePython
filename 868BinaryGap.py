class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        res, last = 0, None
        for i in range(32):
            if (N>>i) & 1:
                if last is not None:
                    res = max(res,i - last)
                last = i
        return res