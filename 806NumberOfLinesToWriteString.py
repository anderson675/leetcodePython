class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 1
        last = 0
        for ch in S:
            width = widths[ord(ch)-ord('a')]
            last += width
            if last > 100:
                line += 1
                last = width
        return [line,last]